import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Daten aus der Tabelle
x_data = np.array([0.189, 0.385, 0.588, 0.682, 0.800])
y_data = np.array([0.195, 0.394, 0.598, 0.690, 0.806])

# Definition der Wurzelfunktion
def wurzel_func(x, a, b):
    return a * np.sqrt(x) + b

# Fit durchführen
popt, _ = curve_fit(wurzel_func, x_data, y_data)
a_fit, b_fit = popt

# Erstellung der Kurve für den Plot
x_fit = np.linspace(0.1, 0.9, 100)
y_fit = wurzel_func(x_fit, a_fit, b_fit)

plt.figure(figsize=(8, 6))

# Messpunkte plotten
plt.scatter(x_data, y_data, color='blue', label='Messwerte')

# Fit-Kurve plotten
plt.plot(x_fit, y_fit, color='green', 
         label='Idealer Kurvenverlauf der Copolymerisation')

# Achsenbeschriftungen und Layout
plt.xlabel('$n_{St} / (n_{St} + n_{MMA})$')
plt.ylabel('$m_{St} / (m_{St} + m_{MMA})$')
plt.title('Copolymerisationsdiagramm')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

plt.tight_layout()
plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Copolymerisation\Bilder\CopoDiagramm.png")
plt.show()

print(f"Ergebnis: a = {a_fit:.4f}, b = {b_fit:.4f}")
