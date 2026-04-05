import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



init = np.array([0.00158, 0.00615, 0.01498])
vbr = np.array([4.26735E-05, 8.40134E-05, 0.00012402])

plt.figure()
plt.plot(init, vbr, "bo" , label="Messdaten")

plt.xscale('log')
plt.yscale('log')

plt.xlabel("log([I])")
plt.ylabel("log([$v_\text{Br}$])")

# 1. Logarithmierung der Daten für den Fit
log_x = np.log10(init)
log_y = np.log10(vbr)

# 2. Linearer Fit (Polynom 1. Grades)
# slope ist die Steigung (Reaktionsordnung), intercept der Achsenabschnitt
slope, intercept = np.polyfit(log_x, log_y, 1)

# 3. Erstellen der Fit-Geraden
# Wir berechnen Werte für die Gerade in der log-Skala
x_fit = np.linspace(min(init), max(init), 100)
# y = 10^(m * log10(x) + b) -> Rücktransformation in den linearen Raum für den Plot
y_fit = 10**(slope * np.log10(x_fit) + intercept)

K_wert = 10**intercept

# 4. Plotten (Ergänzung zum bestehenden Plot)
plt.plot(x_fit, y_fit, 'r-', label=f'Fit (Steigung n = {slope:.2f})')



plt.show()