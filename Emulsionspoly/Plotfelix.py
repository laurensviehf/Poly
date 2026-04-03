import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Die Zielfunktion definieren (Exponentialfunktion)
def exp_funktion(x, a, b):
    return a * np.exp(b * x)

# 2. Beispiel-Daten (mit etwas "Rauschen", damit es realistisch ist)
x_daten = np.array([2, 4, 6, 10, 15, 20, 30, 45, 60, 90, 120, 150, 180])
y_daten = np.array([
    12.59, 8.90, 10.32, 9.13, 10.22, 9.22, 
    8.38, 8.80, 9.99, 10.18, 11.82, 19.66, 59.99
])

# 3. Der Fit: curve_fit findet die optimalen Werte für a und b
parameter, kovarianz = curve_fit(exp_funktion, x_daten, y_daten)
a_fit, b_fit = parameter

print(f"Gefundene Parameter: a = {a_fit:.4f}, b = {b_fit:.4f}")

# 4. Erstellen einer glatten Linie für den Plot der berechneten Funktion
x_fit = np.linspace(0, 5, 100)
y_fit = exp_funktion(x_fit, a_fit, b_fit)

# 5. Visualisierung
plt.figure(figsize=(180, 60))
plt.scatter(x_daten, y_daten, color='red', label='Originaldaten') # Die Punkte
plt.plot(x_fit, y_fit, label=f'Fit: $f(x) = {a_fit:.2f} \cdot e^{{{b_fit:.2f} \cdot x}}$', color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Exponentialer Fit an Datenpunkte')
plt.show()