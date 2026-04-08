import matplotlib.pyplot as plt
import pandas as pd

# Daten laden
df = pd.read_csv(r"D:\Dokumente\Uni laptop\Chemie\Poly\Copolymerisation\trommsdorff_vp_conversion.csv")

# Plot erstellen
plt.plot(df['Umsatz (%)'], df['Reaktionsgeschwindigkeit (v_p)'], label = "$v_p$")
plt.xlabel('Umsatz (%)')
plt.ylabel('$v_p$ (Reaktionsgeschwindigkeit)')
plt.title('Trommsdorff-Effekt: $v_p$ vs. Umsatz')
plt.grid(True)
plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Copolymerisation\Bilder\trommsdorff_vd_conv_plot.png")
plt.show()
