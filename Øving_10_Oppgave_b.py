from datetime import datetime
from main import noe
from Øving_10_Oppgave_a import les_værdata

fil = "snoedybder_vaer_en_stasjon_dogn.csv"

#Sesong = 1 Okt - 1 Juni (1.10 - 1.6)
#Lager liste inni liste med der Sesong[[],[]]
#Indre liste er snødybde og ytre er sesong nr.
sesong = []
nyliste = []
værdata = les_værdata(fil)
NySesong = False
for i in range(len(værdata)):
    start = datetime(værdata[i]["Dato"].year,10,1)
    slutt = datetime(værdata[i]["Dato"].year,6,1)
    #Finner alle dager i sesongen fra 1.1 til 31.5 og 1.10 til 31.12 
    if værdata[i]["Dato"] == datetime(1981,10,31): #Edgecase der sesongen går fra 1980.31.10 til 1981.1.10
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
for n in sesong:
    print(f"Antall dager med skiføre sesongen {year-1}-{year} er {noe(n,20)}")           
    year += 1 

