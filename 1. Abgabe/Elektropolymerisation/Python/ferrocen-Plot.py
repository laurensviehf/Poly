import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Daten einlesen 
# Nutzt den Tabulator als Trennzeichen, wie in der Datei ferrocene.txt zu sehen 
file_path = r'D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Messwerte\ferrocene.txt'
df = pd.read_csv(file_path, sep='\t')

# Spaltennamen definieren 
pot_col = 'Potential applied (V)'
cur_col = 'WE(1).Current (A)'

# 2. Zyklen trennen
# Da die Messung kontinuierlich läuft, teilen wir den Datensatz in 3 gleiche Teile
num_cycles = 3
points_per_cycle = len(df) // num_cycles
cycles = [df.iloc[i*points_per_cycle : (i+1)*points_per_cycle] for i in range(num_cycles)]

# 3. Berechnungen (Peaks und Steigung)
# Wir nutzen den letzten Zyklus für die Peak-Bestimmung (wie in der Grafik)
last_cycle = cycles[-1]
idx_max = last_cycle[cur_col].idxmax()
idx_min = last_cycle[cur_col].idxmin()

e_pa, i_pa = last_cycle.loc[idx_max, pot_col], last_cycle.loc[idx_max, cur_col]
e_pc, i_pc = last_cycle.loc[idx_min, pot_col], last_cycle.loc[idx_min, cur_col]

# Steigung am Nullpunkt (im ersten Zyklus)
target_v = 0
# Finde den Punkt, der 0V am nächsten ist
idx_0 = (cycles[0][pot_col] - target_v).abs().idxmin()
# Numerische Ableitung (Differenzenquotient)
delta_e = df.loc[idx_0 + 1, pot_col] - df.loc[idx_0, pot_col]
delta_i = df.loc[idx_0 + 1, cur_col] - df.loc[idx_0, cur_col]
steigung_0 = delta_i / delta_e

# 4. Visualisierung (Orientierung an grafik.png)
plt.figure(figsize=(10, 7))
colors = ['blue', 'green', 'red']
labels = ['erster Zyklus', 'zweiter Zyklus', 'dritter Zyklus']

for i in range(num_cycles):
    plt.plot(cycles[i][pot_col], cycles[i][cur_col], 
             color=colors[i], label=labels[i], linewidth=1)

# Vertikale Hilfslinien an den Peaks
plt.axvline(x=e_pa, color='grey', linestyle='--', alpha=0.7)
plt.axvline(x=e_pc, color='grey', linestyle='--', alpha=0.7)

# Achsenbeschriftung und Design
plt.xlabel('$E$ (vs Ag/AgCl) in V')
plt.ylabel('$I$ in A')
plt.title('Cyclovoltammogramm von Ferrocen')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')

# Wissenschaftliche Notation für die Strom-Achse
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.tight_layout()

# 5. Text-Ausgabe
print("-" * 30)
print(f"ANALYSE ERGEBNISSE")
print("-" * 30)
print(f"Anodischer Peak (Epa):  {e_pa:.3f} V")
print(f"Kathodischer Peak (Epc): {e_pc:.3f} V")
print(f"Mittelwert:    {(e_pa + e_pc)/2:.3f} V")
print(f"Steigung bei 0V:        {steigung_0:.2e} A/V")
print("-" * 30)

plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Bilder\Ferrocen.png")
plt.show()