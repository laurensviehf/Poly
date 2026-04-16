import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

allDataPath = r"D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Rheology\Messwerte"
savePath = r"D:\Dokumente\Uni laptop\Chemie\Poly\1. Abgabe\Rheology\Bilder"

data = ["20_PVP_amp", "20_PVP_frq"]
dataAMP = pd.read_csv(allDataPath + "\\" + data[0] + ".csv", sep=";", decimal=",")

# Gemeinsame Daten extrahieren
amplitude = dataAMP["Deformation [%]"].to_numpy(dtype=float)
g1 = dataAMP["Speichermodul [Pa]"].to_numpy(dtype=float) 
g2 = dataAMP["Verlustmodul [Pa]"].to_numpy(dtype=float) 
eta = dataAMP["Betrag(Viskosität) [Pa·s]"].to_numpy(dtype=float)

# --- Plot 1: G' ---
plt.figure()
plt.xscale("log")
plt.yscale("log")
plt.plot(amplitude, g1, marker = "o")

plt.xlim(0.005, 10)
plt.xlabel("deformation [%]")
plt.ylabel("G' [Pa]")
plt.tight_layout()
plt.savefig(savePath + r"\20_PVP_amp_G1.png")
plt.show()

# --- Plot 2: G'' ---
plt.figure() # Erstellt ein frisches Fenster
plt.xscale("log")
plt.yscale("log")
plt.plot(amplitude * 1000, g2, marker = "o")

# plt.ylim() wurde entfernt, da es ohne Argumente die Achsen stören kann
plt.xlabel("deformation [%]")
plt.ylabel("G'' [Pa]")
plt.tight_layout()
plt.savefig(savePath + r"\20_PVP_amp_G2.png")
plt.show()

# --- Plot 3: Viskosität ---
plt.figure()
plt.xscale("log")
plt.yscale("log")
plt.plot(amplitude *1000, eta, marker = "o")

plt.xlabel("deformation [%]")
plt.ylabel(r"|$\eta$*| [Pa $\cdot$ s]")
plt.tight_layout()
plt.savefig(savePath + r"\20_PVP_amp_eta.png")
plt.show()