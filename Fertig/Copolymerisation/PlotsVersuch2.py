import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations

# Deine Geradengleichungen: (m, b)
lines = [
    (7.167, -0.139),  # Probe 1
    (3.07, -0.161),   # Probe 2
    (1.754, 0.447),   # Probe 3
    (0.658, 2.263),   # Probe 4
    (0.196, 14.547)   # Probe 5
]

def get_intersection(l1, l2):
    m1, b1 = l1
    m2, b2 = l2
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return np.array([x, y])

def get_incenter(A, B, C):
    # Seitenlängen berechnen
    a = np.linalg.norm(B - C)
    b = np.linalg.norm(A - C)
    c = np.linalg.norm(A - B)
    # Formel für Inkreismittelpunkt
    return (a * A + b * B + c * C) / (a + b + c)

# 1. Alle Inkreismittelpunkte berechnen
all_incenters = []
for combo in combinations(lines, 3):
    # Eckpunkte des Dreiecks aus den 3 Geraden bestimmen
    p1 = get_intersection(combo[0], combo[1])
    p2 = get_intersection(combo[1], combo[2])
    p3 = get_intersection(combo[0], combo[2])
    
    incenter = get_incenter(p1, p2, p3)
    all_incenters.append(incenter)

all_incenters = np.array(all_incenters)
mean_r = np.mean(all_incenters, axis=0)

# --- Plotten ---
plt.figure(figsize=(10, 8))
x_vals = np.linspace(-2, 12, 400)

# Geraden zeichnen
for i, (m, b) in enumerate(lines):
    plt.plot(x_vals, m * x_vals + b, alpha=0.3, label=f'Probe {i+1}')

# Inkreismittelpunkte einzeichnen
plt.scatter(all_incenters[:, 0], all_incenters[:, 1], color='red', 
            marker='o', s=20, label='Inkreismittelpunkte', zorder=5)

# Mittelwert (Ergebnis) hervorheben
plt.scatter(mean_r[0], mean_r[1], color='black', marker='X', 
            s=100, label=f'Mittelwert: $r_{{MMA}}$={mean_r[0]:.2f}, $r_{{St}}$={mean_r[1]:.2f}', zorder=6)

plt.xlim(-1, 15) # Bereich anpassen, um Schnittpunkte zu sehen
plt.ylim(-1, 20)
plt.xlabel('$r_{MMA}$')
plt.ylabel('$r_{St}$')
plt.legend()
plt.grid(True, linestyle='--')
plt.title('Bestimmung der Copolymerisationsparameter (Inkreismethode)')

# --- Konsolenausgabe ---
# Berechnung der Standardabweichung für die Aussage über die Genauigkeit
std_r = np.std(all_incenters, axis=0)

print("-" * 30)
print("ERGEBNIS DER AUSWERTUNG")
print("-" * 30)
print(f"r_MMA (Mittelwert): {mean_r[0]:.4f}")
print(f"r_St  (Mittelwert): {mean_r[1]:.4f}")
print("-" * 30)
print(f"Streuung (Standardabweichung):")
print(f"s(r_MMA) = {std_r[0]:.4f}")
print(f"s(r_St)  = {std_r[1]:.4f}")
print("-" * 30)

# --- Ausgabe der Koordinaten ---
print("\nKoordinaten der Inkreismittelpunkte (r_MMA | r_St):")
print("-" * 40)

for i, center in enumerate(all_incenters, 1):
    # Formatierung auf 4 Nachkommastellen für die Übersichtlichkeit
    print(f"Punkt {i:02d}:  {center[0]:.4f}  |  {center[1]:.4f}")

print("-" * 40)

# Der bereits vorhandene Mittelwert zur Kontrolle
print(f"Mittelwert: {mean_r[0]:.4f}  |  {mean_r[1]:.4f}")


plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Copolymerisation\Bilder\MayoVersuch2.png")
plt.show()