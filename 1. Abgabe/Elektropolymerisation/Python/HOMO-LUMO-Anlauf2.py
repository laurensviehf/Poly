import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# 1. Daten einlesen 
df_homo = pd.read_csv(r'D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Elektropolymerisation\Messwerte\HOMO_P3HT.txt', sep='\t', skiprows=1, names=['Potential applied (V)', 'WE(1).Current (A)'])
df_lumo = pd.read_csv(r'D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Elektropolymerisation\Messwerte\LUMO_P3HT.txt', sep='\t', skiprows=1, names=['Potential applied (V)', 'WE(1).Current (A)'])

# WICHTIGE REPARATUR: Ferrocen-Kalibrierung SOFORT anwenden!
# Dadurch rechnet das gesamte Skript (auch die Peak-Suche) mit den echten, kalibrierten Werten.
df_homo['Potential applied (V)'] = df_homo['Potential applied (V)'] - 0.438
df_lumo['Potential applied (V)'] = df_lumo['Potential applied (V)'] - 0.438

def extract_third_cycle(df):
    """Teilt die CV-Messung in Zyklen auf und extrahiert den dritten Zyklus."""
    voltage = df['Potential applied (V)'].values
    dv = np.diff(voltage)
    signs = np.sign(dv)
    signs[signs == 0] = 1 
    turning_points = np.where(signs[:-1] != signs[1:])[0] + 1
    boundaries = [0] + list(turning_points) + [len(df) - 1]
    
    start_idx = boundaries[4] # Start 3. Zyklus
    end_idx = boundaries[6]   # Ende 3. Zyklus
    
    return df.iloc[start_idx:end_idx]

def get_forward_sweep(df, direction):
    """Extrahiert nur den relevanten Hin-Sweep der Messung."""
    v = df['Potential applied (V)'].values
    i = df['WE(1).Current (A)'].values
    
    if direction == 'up':
        start_idx = np.argmin(v)
        end_idx = np.argmax(v)
        if start_idx > end_idx:
            end_idx = start_idx + np.argmax(v[start_idx:])
    else:
        start_idx = np.argmax(v)
        end_idx = np.argmin(v)
        if start_idx > end_idx:
            end_idx = start_idx + np.argmin(v[start_idx:])
            
    return v[start_idx:end_idx+1], i[start_idx:end_idx+1]

def calc_tangents(v, i, baseline_v_range, peak_v_range, target_peak_idx=0):
    """Berechnet Baseline, Tangente an der aufsteigenden Peak-Flanke und deren Schnittpunkt (Onset)."""
    # 1. Baseline Tangente
    base_mask = (v >= min(baseline_v_range)) & (v <= max(baseline_v_range))
    v_base = v[base_mask]
    i_base = i[base_mask]
    m_base, c_base = np.polyfit(v_base, i_base, 1) 
    
    # 2. Peak Tangente
    peak_mask = (v >= min(peak_v_range)) & (v <= max(peak_v_range))
    v_peak = v[peak_mask]
    i_peak = i[peak_mask]
    
    # Rauschen glätten, um die Ableitung (Steigung) besser zu berechnen
    i_smooth = pd.Series(i_peak).rolling(5, center=True, min_periods=1).mean().values
    di_dv = np.gradient(i_smooth, v_peak)
    
    # Wir suchen NUR nach positiven Steigungen (kein np.abs() mehr)
    peaks, _ = find_peaks(di_dv, height=np.max(di_dv)*0.10)
    
    if len(peaks) > target_peak_idx:
        target_idx = peaks[target_peak_idx]
    elif len(peaks) > 0:
        target_idx = peaks[-1]
    else:
        target_idx = np.argmax(di_dv)
        
    idx_min = max(0, target_idx - 4)
    idx_max = min(len(v_peak), target_idx + 5)
    m_peak, c_peak = np.polyfit(v_peak[idx_min:idx_max], i_peak[idx_min:idx_max], 1)
    
    # 3. Schnittpunkt (Onset) berechnen
    v_onset = (c_peak - c_base) / (m_base - m_peak)
    i_onset = m_base * v_onset + c_base
    
    return m_base, c_base, m_peak, c_peak, v_onset, i_onset


# --- Ausführung ---
cycle3_homo = extract_third_cycle(df_homo)
cycle3_lumo = extract_third_cycle(df_lumo)

# Für HOMO: (Die Suchfenster sind jetzt um -0.438 V verschoben)
v_homo_sw, i_homo_sw = get_forward_sweep(cycle3_homo, 'up')
# Baseline: ~ -0.43 bis -0.28 V | Peak-Suche: ~ -0.23 bis 0.76 V | "0" = Erster Anstieg (Schulter)
m_b_h, c_b_h, m_p_h, c_p_h, v_on_h, i_on_h = calc_tangents(v_homo_sw, i_homo_sw, [-0.438, -0.288], [-0.411, -0.2], 0)

# Für LUMO: (Die Suchfenster sind jetzt ebenfalls um -0.438 V verschoben)
v_lumo_sw, i_lumo_sw = get_forward_sweep(cycle3_lumo, 'down')
# Baseline: ~ -1.23 bis -0.43 V | Peak-Suche: ~ -2.53 bis -1.43 V | "0" = Erster Anstieg
m_b_l, c_b_l, m_p_l, c_p_l, v_on_l, i_on_l = calc_tangents(v_lumo_sw, i_lumo_sw, [-1.238, -0.438], [-2.25, -1.438], 0)


# --- Plotting ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=150)

# Diagramm 1: HOMO
# Beachte: Das '-0.438' im Plot-Befehl ist weg, da wir es oben schon für den kompletten df verrechnet haben!
ax1.plot(cycle3_homo['Potential applied (V)'], cycle3_homo['WE(1).Current (A)'] * 1e6, label='HOMO P3HT', color='blue', linewidth=2)
v_line_h = np.linspace(-0.6, 0.8, 100) 
ax1.plot(v_line_h, (m_b_h * v_line_h + c_b_h) * 1e6, 'k--', label='Erweiterte Baseline')
ax1.plot(v_line_h, (m_p_h * v_line_h + c_p_h) * 1e6, 'g--', label='Peak Tangente (Erste Steigung)')
ax1.plot(v_on_h, i_on_h * 1e6, 'ro', markersize=8, label=f'Onset: {v_on_h:.2f} V')

ax1.set_xlim(-0.7, 0.8)
ax1.set_ylim(-3, cycle3_homo['WE(1).Current (A)'].max()*1e6*1.1)
ax1.set_title('Cyclovoltammetrie: HOMO (Vs. Fc/Fc+)', fontsize=14)
ax1.set_xlabel('Applied Potential (V)', fontsize=12)
ax1.set_ylabel('Current (µA)', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.axhline(0, color='black', linewidth=1)
ax1.axvline(0, color='black', linewidth=1)
ax1.legend(fontsize=10)

# Diagramm 2: LUMO
ax2.plot(cycle3_lumo['Potential applied (V)'], cycle3_lumo['WE(1).Current (A)'] * 1e6, label='LUMO P3HT', color='red', linewidth=2)
v_line_l = np.linspace(-2.6, -0.2, 100)
ax2.plot(v_line_l, (m_b_l * v_line_l + c_b_l) * 1e6, 'k--', label='Erweiterte Baseline')
ax2.plot(v_line_l, (m_p_l * v_line_l + c_p_l) * 1e6, 'g--', label='Peak Tangente')
ax2.plot(v_on_l, i_on_l * 1e6, 'ro', markersize=8, label=f'Onset: {v_on_l:.2f} V')

ax2.set_xlim(-2.7, -0.2)
ax2.set_ylim(cycle3_lumo['WE(1).Current (A)'].min()*1e6*1.1, 3)
ax2.set_title('Cyclovoltammetrie: LUMO (Vs. Fc/Fc+)', fontsize=14)
ax2.set_xlabel('Applied Potential (V)', fontsize=12)
ax2.set_ylabel('Current (µA)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.axhline(0, color='black', linewidth=1)
ax2.axvline(0, color='black', linewidth=1)
ax2.legend(fontsize=10)

plt.tight_layout()

# Plot als Datei speichern und anzeigen
plt.savefig(r'D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Elektropolymerisation\Bilder\P3HT_Tangents.png')
plt.show()

print(f"HOMO Onset ermittelt bei: {v_on_h:.2f} V")
print(f"LUMO Onset ermittelt bei: {v_on_l:.2f} V")