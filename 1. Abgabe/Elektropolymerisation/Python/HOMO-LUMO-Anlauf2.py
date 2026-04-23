import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# --- KONFIGURATION ---
# Die Verschiebung der Potential-Werte (x-Achse)
correction = -0.438 

# Pfade zu den Dateien (bitte hier deine Pfade eintragen)
path_homo = r'C:\Users\laure\Documents\Uni\Chemie\Semester 5\PolyLab\Poly\1. Abgabe\Elektropolymerisation\Messwerte\HOMO_P3HT.txt'
path_lumo = r'C:\Users\laure\Documents\Uni\Chemie\Semester 5\PolyLab\Poly\1. Abgabe\Elektropolymerisation\Messwerte\LUMO_P3HT.txt'
path_save = r'C:\Users\laure\Documents\Uni\Chemie\Semester 5\PolyLab\Poly\1. Abgabe\Elektropolymerisation\Bilder\P3HT_Tangents.png'

# 1. Daten einlesen
df_homo = pd.read_csv(path_homo, sep='\t', skiprows=1, names=['Potential applied (V)', 'WE(1).Current (A)'])
df_lumo = pd.read_csv(path_lumo, sep='\t', skiprows=1, names=['Potential applied (V)', 'WE(1).Current (A)'])

# --- X-WERTE VERSCHIEBEN ---
df_homo['Potential applied (V)'] = df_homo['Potential applied (V)'] + correction
df_lumo['Potential applied (V)'] = df_lumo['Potential applied (V)'] + correction

def extract_third_cycle(df):
    """Teilt die CV-Messung in Zyklen auf und extrahiert den dritten Zyklus."""
    voltage = df['Potential applied (V)'].values
    dv = np.diff(voltage)
    signs = np.sign(dv)
    signs[signs == 0] = 1 
    turning_points = np.where(signs[:-1] != signs[1:])[0] + 1
    boundaries = [0] + list(turning_points) + [len(df) - 1]
    
    # Start und Ende des 3. Zyklus (Indizes basierend auf Wendepunkten)
    start_idx = boundaries[4] 
    end_idx = boundaries[6]   
    return df.iloc[start_idx:end_idx]

def get_forward_sweep(df, direction):
    """Extrahiert den Hin-Sweep (Anstieg oder Abfall) der Messung."""
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

def calc_tangents_horizontal(v, i, baseline_v_range, peak_v_range, target_peak_idx=0):
    """Berechnet horizontale Baseline, Peak-Tangente und den Onset-Schnittpunkt."""
    # 1. Horizontale Baseline (m = 0)
    base_mask = (v >= min(baseline_v_range)) & (v <= max(baseline_v_range))
    i_base_values = i[base_mask]
    
    m_base = 0.0
    c_base = np.mean(i_base_values) # Mittelwert des Stroms im Bereich
    
    # 2. Peak Tangente
    peak_mask = (v >= min(peak_v_range)) & (v <= max(peak_v_range))
    v_peak = v[peak_mask]
    i_peak = i[peak_mask]
    
    # Glättung für stabilere Ableitung
    i_smooth = pd.Series(i_peak).rolling(5, center=True, min_periods=1).mean().values
    di_dv = np.gradient(i_smooth, v_peak)
    
    # Suche nach Peaks in der Steigung
    peaks, _ = find_peaks(di_dv, height=np.max(di_dv)*0.10)
    
    if len(peaks) > target_peak_idx:
        target_idx = peaks[target_peak_idx]
    elif len(peaks) > 0:
        target_idx = peaks[-1]
    else:
        target_idx = np.argmax(di_dv)
        
    # Lokale Regression am Punkt der maximalen Steigung
    idx_min = max(0, target_idx - 4)
    idx_max = min(len(v_peak), target_idx + 5)
    m_peak, c_peak = np.polyfit(v_peak[idx_min:idx_max], i_peak[idx_min:idx_max], 1)
    
    # 3. Schnittpunkt (Onset) berechnen
    # Gleichung: c_base = m_peak * v_onset + c_peak
    v_onset = (c_base - c_peak) / m_peak
    i_onset = c_base 
    
    return m_base, c_base, m_peak, c_peak, v_onset, i_onset

# --- Ausführung der Analyse ---
cycle3_homo = extract_third_cycle(df_homo)
cycle3_lumo = extract_third_cycle(df_lumo)

# Analyse HOMO (Hin-Sweep aufwärts)
v_homo_sw, i_homo_sw = get_forward_sweep(cycle3_homo, 'up')
m_b_h, c_b_h, m_p_h, c_p_h, v_on_h, i_on_h = calc_tangents_horizontal(
    v_homo_sw, i_homo_sw, 
    [0.0 + correction, 0.1 + correction], # Baseline Bereich
    [0.1 + correction, 1.2 + correction], # Peak Bereich
    2
)

# Analyse LUMO (Hin-Sweep abwärts)
v_lumo_sw, i_lumo_sw = get_forward_sweep(cycle3_lumo, 'down')
m_b_l, c_b_l, m_p_l, c_p_l, v_on_l, i_on_l = calc_tangents_horizontal(
    v_lumo_sw, i_lumo_sw, 
    [-0.8 + correction, 0.0 + correction], # Baseline Bereich
    [-1.8 + correction, -1.0 + correction], # Peak Bereich
    0
)

# --- Plotting ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=150)

# Diagramm 1: HOMO
ax1.plot(cycle3_homo['Potential applied (V)'], cycle3_homo['WE(1).Current (A)'] * 1e6, label='HOMO P3HT', color='blue', lw=2)
v_line_h = np.linspace(-0.2 + correction, 1.2 + correction, 100) 
ax1.axhline(c_b_h * 1e6, color='black', ls='--', label='Horizontale Baseline')
ax1.plot(v_line_h, (m_p_h * v_line_h + c_p_h) * 1e6, 'g--', label='Peak Tangente')
ax1.plot(v_on_h, i_on_h * 1e6, 'ro', ms=8, label=f'Onset: {v_on_h:.2f} V')

ax1.set_xlim(-0.2 + correction, 1.2 + correction)
ax1.set_title('Cyclovoltammetrie: HOMO (Korrigiert)', fontsize=14)
ax1.set_xlabel('Potential (V) [vs. Ref]', fontsize=12)
ax1.set_ylabel('Current (µA)', fontsize=12)
ax1.grid(True, ls='--', alpha=0.6)
ax1.legend(fontsize=9)

# Diagramm 2: LUMO
ax2.plot(cycle3_lumo['Potential applied (V)'], cycle3_lumo['WE(1).Current (A)'] * 1e6, label='LUMO P3HT', color='red', lw=2)
v_line_l = np.linspace(-2.1 + correction, 0.2 + correction, 100)
ax2.axhline(c_b_l * 1e6, color='black', ls='--', label='Horizontale Baseline')
ax2.plot(v_line_l, (m_p_l * v_line_l + c_p_l) * 1e6, 'g--', label='Peak Tangente')
ax2.plot(v_on_l, i_on_l * 1e6, 'ro', ms=8, label=f'Onset: {v_on_l:.2f} V')

ax2.set_xlim(-2.2 + correction, 0.2 + correction)
ax2.set_ylim(-150, 5)
ax2.set_title('Cyclovoltammetrie: LUMO (Korrigiert)', fontsize=14)
ax2.set_xlabel('Potential (V) [vs. Ref]', fontsize=12)
ax2.set_ylabel('Current (µA)', fontsize=12)
ax2.grid(True, ls='--', alpha=0.6)
ax2.legend(fontsize=9)

plt.tight_layout()
plt.savefig(path_save)
plt.show()

print(f"HOMO Onset: {v_on_h:.3f} V (korrigiert)")
print(f"LUMO Onset: {v_on_l:.3f} V (korrigiert)")