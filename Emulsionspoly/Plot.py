import matplotlib.pyplot as plt
import numpy as np




# 1. Daten aus der Tabelle extrahieren
# Zeit t in Minuten
zeit = [2, 4, 6, 10, 15, 20, 30, 45, 60, 90, 120, 150, 180]

# Umsatz in Prozent
umsatz = [
    12.59, 8.90, 10.32, 9.13, 10.22, 9.22, 
    8.38, 8.80, 9.99, 10.18, 11.82, 19.66, 59.99
]

def exp_funktion(x, a, b):
    return a * np.exp(b * x)

# 2. Plot initialisieren
plt.figure(figsize=(10, 6))

# Kurve mit Markern zeichnen
plt.plot(zeit, umsatz, marker='o', linestyle='-', color='b', 
         linewidth=2, markersize=6, label='Reaktionsumsatz')

# 3. Achsenbeschriftung (LaTeX für Symbole)
plt.xlabel('Zeit $t$ [min]', fontsize=12)
plt.ylabel('Umsatz [$\\%$]', fontsize=12)
plt.title('Umsatz-Zeit-Diagramm', fontsize=14)

# 4. Diagramm-Feinschliff
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()

# 5. Speichern und Anzeigen
# plt.savefig('umsatz_plot.png', dpi=300) # Optional zum Speichern
plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Emulsionspoly\Bilder\UmsatzZeitPlot.png")
plt.show()