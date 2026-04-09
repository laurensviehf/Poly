import matplotlib.pyplot as plt
import numpy as np

# Daten aus der Tabelle (Python nutzt Punkte als Dezimaltrennzeichen)
# x = n_St^2/n_MMA^2 * 1/(m_St/m_MMA)
# y = n_St/n_MMA * (1 - 1/(m_St/m_MMA))
x = np.array([0.224, 0.601, 1.373, 2.060, 3.845])
y = np.array([-0.728, -0.336, 0.467, 1.182, 3.039])

# Lineare Regression (1. Grades)
# m = Steigung, b = Achsenabschnitt
m, b = np.polyfit(x, y, 1)

# Werte für die Ausgleichsgerade berechnen
x_fit = np.linspace(min(x), max(x), 100)
y_fit = m * x_fit + b

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Messdaten (Fineman-Ross-Terme)', zorder=5)
plt.plot(x_fit, y_fit, color='blue', linestyle='--', label=f'Ausgleichsgerade: y = {m:.4f}x + ({b:.4f})')

# Achsenbeschriftungen
plt.xlabel(r'$\frac{n_{St}^2}{n_{MMA}^2} \cdot \frac{1}{m_{St}/m_{MMA}}$')
plt.ylabel(r'$\frac{n_{St}}{n_{MMA}} \cdot \left(1 - \frac{1}{m_{St}/m_{MMA}}\right)$')
plt.title('Fineman-Ross-Plot zur Ermittlung von $r_1$ und $r_2$')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

# Konsolenausgabe
print("-" * 30)
print("LINEARE REGRESSION")
print("-" * 30)
print(f"Steigung (m):       {m:10.4f}")
print(f"Achsenabschnitt (b): {b:10.4f}")
print("-" * 30)
# Interpretation im Kontext der Copolymerisation
print(f"Daraus folgt (theoretisch):")
print(f"r_1 (Styrol)  ≈ {m:.4f}")
print(f"r_2 (MMA)     ≈ {-b:.4f}")
print("-" * 30)

plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Copolymerisation\Bilder\GraphFineman.png")
plt.show()