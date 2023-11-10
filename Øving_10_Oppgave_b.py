from Øving_10_Oppgave_a import les_værdata

fil = "snoedybder_vaer_en_stasjon_dogn.csv"

#Sesong = 1 Okt - 1 Juni (1.10 - 1.6)
værdata = les_værdata(fil)
print(værdata[1]["Dato"])