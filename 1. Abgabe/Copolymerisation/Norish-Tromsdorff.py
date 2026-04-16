import pandas as pd
import matplotlib.pyplot as plt

# 1. Daten einlesen
try:
    df = pd.read_csv('trommsdorff_vp_conversion.csv')
except FileNotFoundError:
    print("Die Datei 'trommsdorff_vp_conversion.csv' wurde nicht gefunden.")
    exit()

# 2. Plot erstellen
plt.figure(figsize=(100, 1))

# Hauptkurve: v_p über Umsatz
plt.plot(df['Umsatz (%)'], df['Reaktionsgeschwindigkeit (v_p)'], 
         color='blue', linewidth=2.5, label='Reaktionsgeschwindigkeit $v_p$')

# 3. Markierung des Geleffekts (optional, zur Verdeutlichung)
# Wir suchen den Punkt, an dem v_p nach dem Minimum wieder steigt
v_p_min_idx = df['Reaktionsgeschwindigkeit (v_p)'].idxmin()
plt.axvline(x=df.iloc[v_p_min_idx]['Umsatz (%)'], color='red', 
            linestyle='--', alpha=0.6, label='Beginn Geleffekt (Autoakzeleration)')

# 4. Styling
plt.title('Norrish-Trommsdorff-Effekt: Geschwindigkeit vs. Umsatz', fontsize=14)
plt.xlabel('Umsatz (%)', fontsize=12)
plt.ylabel('Reaktionsgeschwindigkeit $v_p$ [mol/(L·s)]', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# 5. Anzeigen
plt.tight_layout()
plt.show()