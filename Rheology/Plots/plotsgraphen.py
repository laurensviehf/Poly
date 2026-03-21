import matplotlib.pyplot as plt
import numpy as np

# 1. Daten vorbereiten
# Wir erstellen 400 Punkte zwischen 0 und 5 für eine glatte Kurve
x = np.linspace(0, 50, 4000)

# 2. Funktionen definieren
y_gerade = np.full_like(x,4)              # Lineare Funktion
y_parabel =  4 + np.exp(x-4)           # Quadratische Funktion
y_wurzel =  -np.exp(x-4) + 4       # Wurzelfunktion

# 3. Plot erstellen

plt.plot(x, y_gerade, label='newtonian', color='blue', linestyle='--')
plt.plot(x, y_parabel, label='shear-thickenning', color='red')
plt.plot(x, y_wurzel, label='shear-thinning', color='green')

# 4. Design-Elemente hinzufügen
plt.xlabel(r'shear rate [$\dot\gamma_0$]')
plt.ylabel(r'shear-stress [$\tau$]')
#plt.axhline(0, color='black', linewidth=0.5) # x-Achse
#plt.axvline(0, color='black', linewidth=0.5) # y-Achse
plt.legend() # Zeigt die Beschriftungen an

# Limitieren der y-Achse, damit die Parabel das Bild nicht "sprengt"
plt.xticks([])
plt.yticks([])
plt.ylim(2, 6)
plt.xlim(0, 5)

plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Bilder" + "\\" + "fließgraph")
