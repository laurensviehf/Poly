import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema

# 1. Daten laden
file_name = r'D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Messwerte\Electropoly_EDOT.txt'
df = pd.read_csv(file_name, sep='\t')
df.columns = [c.strip() for c in df.columns]

pot = df.iloc[:, 0].values - 0.438
cur = df.iloc[:, 1].values

# 2. Zyklen erkennen (Suche nach den Umkehrpunkten am unteren Ende)
# Wir suchen lokale Minima im Potentialverlauf
minima_indices = argrelextrema(pot, np.less, order=100)[0]

# Wir definieren die Grenzen: Start, die gefundenen Minima, und das Ende
boundaries = [0] + list(minima_indices) + [len(pot)]

# 3. Plotten der 3 Zyklen
plt.figure(figsize=(10, 7))
colors = ['blue', 'green', 'red']
labels = ['erster Zyklus', 'zweiter Zyklus', 'dritter Zyklus']

# Wir plotten nur bis maximal 3 Zyklen
num_cycles = min(3, len(boundaries) - 1)

for i in range(num_cycles):
    start, end = boundaries[i], boundaries[i+1]
    plt.plot(pot[start:end], cur[start:end], 
             label=labels[i], color=colors[i], linewidth=1.5)

# 4. Optik & Achsen (Orientierung an deiner Vorlage)
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')

plt.title('EDOT Elektropolymerisation (3 Zyklen)', fontsize=14)
plt.xlabel('Potential $E$ (vs. $\mathrm{Fc/Fc^+}$) / V', fontsize=12)
plt.ylabel('Stromstärke $I$ / A', fontsize=12)

# Wissenschaftliche Notation für kleine Ströme
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Elektropolymerisation\Bilder\EDOT.png")
plt.show()