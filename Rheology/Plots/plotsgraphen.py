import matplotlib.pyplot as plt
import numpy as np

# 1. Daten vorbereiten
# Wir erstellen 400 Punkte zwischen 0 und 5 für eine glatte Kurve
x = np.linspace(0, 50, 4000)

# 2. Funktionen definieren
y_gerade = 4                # Lineare Funktion
y_parabel =  4 + np.exp()           # Quadratische Funktion
y_wurzel =  np.sqrt(x)       # Wurzelfunktion

# 3. Plot erstellen
plt.figure(figsize=(10, 6))

plt.plot(x, y_gerade, label='newtonian', color='blue', linestyle='--')
plt.plot(x, y_parabel, label='shear-thickenning', color='red')
plt.plot(x, y_wurzel, label='shear-thinning', color='green')

# 4. Design-Elemente hinzufügen
plt.xlabel(r'shear rate [$\dot\gamma_0$]')
plt.ylabel(r'shear-stress [$\tau$]')
plt.axhline(0, color='black', linewidth=0.5) # x-Achse
plt.axvline(0, color='black', linewidth=0.5) # y-Achse
plt.legend() # Zeigt die Beschriftungen an

# Limitieren der y-Achse, damit die Parabel das Bild nicht "sprengt"
plt.ylim(0, 50)

plt.savefig(r"C:\Users\rothf\OneDrive\Dokumente\Chemie\Latex_Laurens\Poly\Rheology\Bilder" + "\\" + "Fliesgraph")
