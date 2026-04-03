import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Daten definieren
zeit = np.array([2, 4, 6, 10, 15, 20, 30, 45, 60, 90, 120, 150, 180])
umsatz = np.array([12.591, 8.897, 10.322, 9.126, 10.220, 9.220, 
                   8.378, 8.805, 9.986, 10.179, 11.816, 19.664, 59.994])

# 2. Fit-Funktion: Exponentielles Wachstum
def exp_funktion(t, a, b, c):
    return a * np.exp(b * t) + c

# Startwerte schätzen
p_start = [0.1, 0.03, 9]

try:
    popt, _ = curve_fit(exp_funktion, zeit, umsatz, p0=p_start, maxfev=10000)
    print("Exponential-Fit erfolgreich!")
except Exception as e:
    print(f"Fehler beim Fitten: {e}")

# 3. Kontinuierliche Daten für die Kurven berechnen
t_plot = np.linspace(0, 180, 500)
u_plot = exp_funktion(t_plot, *popt)

# Ableitung (Geschwindigkeit v): v = a * b * e^(bt)
def v_exp(t, a, b):
    return a * b * np.exp(b * t)

v_plot = v_exp(t_plot, popt[0], popt[1])

# 4. Visualisierung
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Plot 1: Umsatz
ax1.scatter(zeit, umsatz, color='red', label='Messdaten')
ax1.plot(t_plot, u_plot, 'b-', label='Fit des Umsatz-Zeit-Diagramms')
ax1.set_ylabel('Umsatz [%]', fontsize=12)
ax1.set_title('Umsatz-Zeit-Kurve', fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.legend()

# Plot 2: Geschwindigkeit
ax2.plot(t_plot, v_plot, 'g-', linewidth=2, label='Reaktionsgeschwindigkeit $v = du/dt$')
ax2.set_xlabel('Zeit $t$ [min]', fontsize=12)
ax2.set_ylabel('v [%/min]', fontsize=12)
ax2.set_title('Reaktionsgeschwindigkeit', fontsize=14)
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
# Pfad zum Speichern (angepasst an deinen PC)
plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Emulsionspoly\Bilder\UmsatzZeitPlot.png")
plt.show()

# 5. Vollständige Ergebnistabelle für alle Messpunkte
print(f"\nBerechnete Geschwindigkeiten für alle Messpunkte:")
print("-" * 55)
print(f"{'Zeit [min]':^12} | {'Umsatz [%]':^12} | {'v [%/min]':^15}")
print("-" * 55)

for t_val, u_val in zip(zeit, umsatz):
    # Berechnung der Geschwindigkeit v am exakten Zeitpunkt t des Messpunkts
    v_punkt = v_exp(t_val, popt[0], popt[1])
    print(f"{t_val:^12} | {u_val:^12.3f} | {v_punkt:^15.4f}")

print("-" * 55)