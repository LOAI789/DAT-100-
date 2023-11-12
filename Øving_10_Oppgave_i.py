from Øving_10_Oppgave_a import les_værdata
from main import diff
import matplotlib.pyplot as plt 
import numpy as np


fil = "snoedybder_vaer_en_stasjon_dogn.csv"
værdata = les_værdata(fil)

CurrentMonth = 0
CurrentYear = 0
gjennomsnitt = []
tempListe = [0]
for i in range (len(værdata)):
    #Skjekker hvis vi fortsatt er i samme måned og år.
    if værdata[i]["Dato"].month == CurrentMonth and værdata[i]["Dato"].year == CurrentYear:
        tempListe.append(værdata[i]["Middeltemperatur"])
    #Når ny måned eller år => Finner gjennomsnitt av forrige måned og legger i liste gjennomsnitt
    elif værdata[i]["Dato"].month != CurrentMonth or værdata[i]["Dato"].year != CurrentYear:
        CurrentYear = værdata[i]["Dato"].year
        CurrentMonth = værdata[i]["Dato"].month
        ListWithoutNone = [i for i in tempListe if i is not None]
        #Det er en måned som ikke har verdier for temp
        try:
            gjennomsnitt.append(sum(ListWithoutNone)/len(ListWithoutNone))
        except ZeroDivisionError:
            print("Ingen temperaturer")
        tempListe = [værdata[i]["Middeltemperatur"]]


gjennomsnitt.pop(0)
#Bruker funksjon fra oppgave 1e til å lage en ny liste med differanse
differanse = diff(gjennomsnitt)


y = gjennomsnitt
x = np.linspace(1980,2023,len(gjennomsnitt))
x2 = np.linspace(1980,2023,len(differanse))
plt.ylabel("Temperatur")
plt.xlabel("År")
plt.plot(x,y,label ="Gjennomsnitt måned")
plt.plot(x2,differanse,label ="Differanse måned")
plt.legend()
plt.show()
