#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:29:31 2023

@author: havardalme
"""

import matplotlib.pyplot as plt
from datetime import datetime
from Øving_10_oppgave_a import les_værdata
from oppgave_g import calculate_trend

fil = "snoedybder_vaer_en_stasjon_dogn.csv"


sesong = []
nyliste = []
værdata = les_værdata(fil)
NySesong = False
for i in range(len(værdata)):
    start = datetime(værdata[i]["Dato"].year,10,1)
    slutt = datetime(værdata[i]["Dato"].year,6,1)

    if værdata[i]["Dato"] == datetime(1981,10,31): 
         NySesong = True 
    elif start <= værdata[i]["Dato"] or værdata[i]["Dato"] < slutt: 
        if NySesong == True:
           sesong.append(nyliste)  
           nyliste = []
           NySesong = False
        nyliste.append(værdata[i]["Snødybde"])
    elif værdata[i]["Dato"] < start and værdata[i]["Dato"] > slutt :
            NySesong = True

year = 1980


skiføre_per_sesong = []
dager_med_data_per_sesong = []
for n in sesong:
    dager_med_data_per_sesong.append(len(n))
    skiføre_per_sesong.append(noe(n, 20))


filtrerte_skiføre = [skiføre for skiføre, dager in zip(skiføre_per_sesong, dager_med_data_per_sesong) if dager >= 200]
filtrerte_årstall = [startår for startår, dager in zip(range(1980, 1980 + len(skiføre_per_sesong)), dager_med_data_per_sesong) if dager >= 200]

a, b = calculate_trend(filtrerte_årstall, filtrerte_skiføre)
   
plt.scatter(filtrerte_årstall, filtrerte_skiføre, label='Dager med skiføre')
trend_y = [a * x + b for x in filtrerte_årstall]
plt.plot(filtrerte_årstall, trend_y, label='Trendlinje', color='red')

plt.title('Antall Dager med Skiføre og Trendlinje')
plt.xlabel('År')
plt.ylabel('Antall Dager med Skiføre')

plt.legend()   
plt.show()
