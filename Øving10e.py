#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:15:27 2023

@author: havardalme
"""

import matplotlib.pyplot as plt
from datetime import datetime
from Øving_10_oppgave_a import les_værdata

def liste_tall_over_5(liste):
    sum = 0
    for element in liste:
        if element > 5:
            sum += element - 5
    return sum


fil = "snoedybder_vaer_en_stasjon_dogn.csv"
værdata = les_værdata(fil)


temp_per_år = {}
for data in værdata:
    år = data["Dato"].year
    temp = data["Middeltemperatur"]
    if temp is not None:
        if år in temp_per_år:
            temp_per_år[år].append(temp)
        else:
            temp_per_år[år] = [temp]


vekst_per_år = {}
for år, temperaturer in temp_per_år.items():
    if len(temperaturer) >= 300:
        vekst_per_år[år] = liste_tall_over_5(temperaturer)


årstall = list(vekst_per_år.keys())
vekst = list(vekst_per_år.values())

plt.plot(årstall, vekst, marker='o')
plt.title('Plantevekst per År')
plt.xlabel('År')
plt.ylabel('Plantevekst basert på Temperatur')
plt.show()
