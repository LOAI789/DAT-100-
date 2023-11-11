from Øving_10_Oppgave_a import les_værdata
from main import diff
import matplotlib.pyplot as plt 
import numpy as np


fil = "snoedybder_vaer_en_stasjon_dogn.csv"
værdata = les_værdata(fil)

CurrentMonth = 0
CurrentYear = 0
gjennomsnitt = []
navn = [0]
for i in range (len(værdata)):
    if værdata[i]["Dato"].month == CurrentMonth and værdata[i]["Dato"].year == CurrentYear:
        navn.append(værdata[i]["Middeltemperatur"])
    elif værdata[i]["Dato"].month != CurrentMonth or værdata[i]["Dato"].year != CurrentYear:
        CurrentYear = værdata[i]["Dato"].year
        CurrentMonth = værdata[i]["Dato"].month
        ListWithoutNone = [i for i in navn if i is not None]
        print(ListWithoutNone)
        try:
            gjennomsnitt.append(sum(ListWithoutNone)/len(ListWithoutNone))
        except ZeroDivisionError:
            print("Ingen temperaturer")
        navn = [værdata[i]["Middeltemperatur"]]
        
gjennomsnitt.pop(0)

differanse = diff(gjennomsnitt)
print(differanse)
y = gjennomsnitt
x = np.linspace(1980,2023,len(gjennomsnitt))
x2 = np.linspace(1980,2023,len(differanse))
plt.ylabel("Temperatur")
plt.xlabel("År")
plt.plot(x,y,label ="Gjennomsnitt måned")
plt.plot(x2,differanse,label ="Differanse måned")
plt.legend()
plt.show()
