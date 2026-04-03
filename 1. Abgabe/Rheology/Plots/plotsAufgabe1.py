import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import LogLocator, LogFormatterExponent, ScalarFormatter

allDataPath = r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Messwerte"

data = ["14_PVP", "Honey", "Speisestärke"]

for i in data:
    dataI = pd.read_csv(allDataPath + "\\" + i + ".csv", sep = ";", decimal = ",")

    schubspannung = dataI["Schubspannung [Pa]"].to_numpy(dtype=float)
    scherrate = dataI["Scherrate [1/s]"].to_numpy(dtype=float)
    viskosität = dataI["Viskosität [Pa·s]"].to_numpy(dtype=float)

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color1 = 'tab:blue'
    ax1.set_xlabel('Deformation velocity [1/s]')
    ax1.set_ylabel('shear stress [Pa]', color=color1)
    line1, = ax1.plot(scherrate, schubspannung, color=color1, marker='o', label='shear stress')
    ax1.tick_params(axis='y')
    ax1.set_xscale('log') # Logarithmische x-Achse ist bei Rheologie üblich
    ax1.set_yscale('log')

    ax2 = ax1.twinx()

    color2 = 'tab:red'
    ax2.set_ylim(1e-2, 500) 
    ax2.set_ylabel('viscosity [Pa·s]', color=color2)
    line2, = ax2.plot(scherrate, viskosität, color=color2, marker='s', label='viscosity')
    ax2.tick_params(axis='y')
    ax2.set_yscale('log')

    lines = [line1, line2]
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left')

    fig.tight_layout() # Verhindert, dass Beschriftungen abgeschnitten werden
    plt.savefig(r"D:\Dokumente\Uni laptop\Chemie\Poly\Rheology\Bilder" + "\\" + i)



