# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 15:09:24 2025

@author: Selene
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Parameters van het systeem
m = 0.200  # massa in kg
k = 0.11   # veerconstante in N/m
c = 0.80   # dempingconstante in Ns/m

# Inlezen van tijd en uitwijking x(t) uit CSV bestand
with open('meting2NC.csv') as file:
    reader = csv.reader(file) 
    next(reader)  # sla kopregel over
    data = np.array([[float(r[0]), float(r[1])] for r in reader])
    tijd, x_input = data[:, 0], data[:, 1]

# Initialisatie
dt = tijd[1] - tijd[0]
x = x_input - 0.073  # uitwijking
v = np.zeros_like(tijd)  # snelheid
a_sensor = np.zeros_like(tijd)  # versnelling via model (a = kx/m)

# Berekening van snelheid v(t)
for i in range(1, len(tijd)):
    v[i] = (x[i] - x[i-1]) / dt

# Berekening van modelversnelling a_sensor(t)
for i in range(1, len(tijd)):
    a_sensor[i] = (k * x[i]) / m

# Plotten van modelversnelling
plt.figure(figsize=(9, 5))
plt.plot(tijd, a_sensor, color='blue', label='Modelversnelling a = kx/m')
plt.xlabel('Tijd (s)')
plt.ylabel('Versnelling (m/s²)')
plt.title('Modelversnelling van massa-veer-demper-systeem')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Exporteren van resultaten naar CSV
df = pd.DataFrame({
    "tijd (s)": np.round(tijd, 5),
    "x (m)": np.round(x, 5),
    "v (m/s)": np.round(v, 5),
    "a_model (m/s²)": np.round(a_sensor, 5)
})

df.to_csv("output_versnellingssensor.csv", index=False, sep=';')
print(df)