import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Pfade
path_homo = r'D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Messwerte\HOMO_P3HT.txt'
path_lumo = r'D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Messwerte\LUMO_P3HT.txt'
save_path = r'D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Bilder\P3HT_Full_Onsets.png'

correction = 0.438

# --- MANUELLE JUSTIERUNG (Intervalle für die Regression) ---
HOMO_base_lim = (-0.1, 0.1)
HOMO_slope_lim = (0.45, 0.55)

LUMO_base_lim = (-1.4, -1.0)    # Waagerechter Bereich vor der Reduktion
LUMO_slope_lim = (-1.68, -1.62) # Erster Abfall (Schulter)
# -----------------------------------------------------------

def get_data(path):
    df = pd.read_csv(path, sep='\t')
    df.columns = [c.strip() for c in df.columns]
    pot = df.iloc[:, 0].values - correction
    cur = df.iloc[:, 1].values
    return pot, cur

def get_line_params(x, y, limits):
    """Schritt 1: Erstellt die Tangente (lineare Regression) für ein Intervall."""
    mask = (x >= min(limits)) & (x <= max(limits))
    if not any(mask):
        return None
    # Berechnet Steigung (m) und y-Achsenabschnitt (c)
    m, c = np.polyfit(x[mask], y[mask], 1)
    return m, c

def calculate_intersection(line1, line2):
    """Schritt 2: Ermittelt den Schnittpunkt zweier Geraden m1*x + c1 = m2*x + c2."""
    m1, c1 = line1
    m2, c2 = line2
    # x = (c2 - c1) / (m1 - m2)
    x_intersect = (c2 - c1) / (m1 - m2)
    return x_intersect

def process_onset(ax, p, c, base_lim, slope_lim, title):
    # Alle Daten plotten
    ax.plot(p, c, color='black', alpha=0.3, label='Messdaten')
    
    # 1. Tangenten-Parameter ermitteln
    params_base = get_line_params(p, c, base_lim)
    params_slope = get_line_params(p, c, slope_lim)
    
    if params_base and params_slope:
        # 2. Schnittpunkt (Onset) berechnen
        onset_x = calculate_intersection(params_base, params_slope)
        onset_y = params_base[0] * onset_x + params_base[1]
        
        # Tangenten für den Plot vorbereiten
        x_vals = np.linspace(min(p), max(p), 1000)
        y_base = params_base[0] * x_vals + params_base[1]
        y_slope = params_slope[0] * x_vals + params_slope[1]
        
        # Zeichnen
        ax.plot(x_vals, y_base, 'r--', lw=1.5, label='Basis-Tangente')
        ax.plot(x_vals, y_slope, 'g--', lw=1.5, label='Steigungs-Tangente')
        ax.plot(onset_x, onset_y, 'ro', ms=8)
        
        ax.annotate(f'Onset: {onset_x:.3f} V', (onset_x, onset_y), xytext=(25, 25),
                    textcoords='offset points', arrowprops=dict(arrowstyle='->', color='red'),
                    bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.8))

    ax.set_title(title, fontsize=14)
    ax.set_xlim(min(p), max(p))
    ax.set_ylim(min(c)*1.1, max(c)*1.1)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()

try:
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 11))

    # Daten laden
    p_h, c_h = get_data(path_homo)
    p_l, c_l = get_data(path_lumo)

    # Verarbeitung
    process_onset(ax1, p_h, c_h, HOMO_base_lim, HOMO_slope_lim, 'P3HT HOMO Onset')
    process_onset(ax2, p_l, c_l, LUMO_base_lim, LUMO_slope_lim, 'P3HT LUMO Onset')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

except Exception as e:
    print(f"Fehler: {e}. Bitte Intervalle prüfen!")