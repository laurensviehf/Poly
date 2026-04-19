import pandas as pd
import matplotlib.pyplot as plt

# 1. Daten einlesen
# Tipp: Deine TXT-Datei ist tabulatorgetrennt, daher nutzen wir sep='\t'
daten = pd.read_csv(r'D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Elektropolymerisation\Messwerte\LUMO_P3HT.txt', sep='\t')

# Lass uns kurz überprüfen, wie die Spaltennamen exakt heißen
# print(daten.columns) 

# 2. Plot initialisieren
plt.figure(figsize=(8, 6))

# 3. Daten plotten
# Die Spaltennamen aus deiner Datei lauten "Potential applied (V)" und "WE(1).Current (A)"
plt.plot(daten['Potential applied (V)'], daten['WE(1).Current (A)'], color='blue', label='P3HT')

# 4. Achsen beschriften - Hier bist du gefragt!
plt.xlabel('DEINE X-ACHSEN BESCHRIFTUNG HIER') 
plt.ylabel('DEINE Y-ACHSEN BESCHRIFTUNG HIER')
plt.title('Cyclovoltammetrie von P3HT')

# 5. Feinschliff: Raster und Legende hinzufügen
plt.grid(True)
plt.legend()

# 6. Diagramm anzeigen lassen
plt.show()