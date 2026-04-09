import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema

# 1. Konfiguration & Pfade
path_homo = r'D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Messwerte\HOMO_P3HT.txt'
path_lumo = r'D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Messwerte\LUMO_P3HT.txt'
save_path_cycles = r'D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Bilder\P3HT_Zyklen.png'

correction = 0.438
colors = ['blue', 'green', 'red']
labels = ['1. Zyklus', '2. Zyklus', '3. Zyklus']

def get_cycles(path):
    """Lädt Daten und gibt eine Liste von (Potential, Strom)-Tupeln pro Zyklus zurück."""
    df = pd.read_csv(path, sep='\t')
    df.columns = [c.strip() for c in df.columns]
    pot = df.iloc[:, 0].values - correction
    cur = df.iloc[:, 1].values
    
    # Zyklen finden (basierend auf Minima des Potentials)
    mins = argrelextrema(pot, np.less, order=100)[0]
    boundaries = [0] + list(mins) + [len(pot)]
    
    cycles = []
    for i in range(min(3, len(boundaries) - 1)):
        start, end = boundaries[i], boundaries[i+1]
        cycles.append((pot[start:end], cur[start:end]))
    return cycles

try:
    # Daten laden
    homo_cycles = get_cycles(path_homo)
    lumo_cycles = get_cycles(path_lumo)

    # --- BILD 1: Normale Zyklen-Übersicht ---
    fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    # HOMO Plot
    for i in range(len(homo_cycles)):
        ax1.plot(homo_cycles[i][0], homo_cycles[i][1], color=colors[i], label=labels[i])
    
    # LUMO Plot
    for i in range(len(lumo_cycles)):
        ax2.plot(lumo_cycles[i][0], lumo_cycles[i][1], color=colors[i], label=labels[i])
    
    ax1.set_title('P3HT: HOMO Bereich (Oxidation)')
    ax2.set_title('P3HT: LUMO Bereich (Reduktion)')
    
    for ax in [ax1, ax2]:
        ax.axhline(0, color='black', lw=0.8)
        ax.axvline(0, color='black', lw=0.8)
        ax.set_xlabel('Potential $E$ (vs. $\mathrm{Fc/Fc^+}$) / V')
        ax.set_ylabel('Stromstärke $I$ / A')
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        ax.grid(True, linestyle=':', alpha=0.5)
        ax.legend()
    
    plt.tight_layout()
    plt.savefig(save_path_cycles, dpi=300)
    plt.show()

except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")