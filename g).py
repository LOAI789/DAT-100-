import matplotlib.pyplot as plt
from datetime import datetime

def float_konvertering(verdi):
    try:
        return float(verdi.replace(',', '.'))
    except ValueError:
        return None

def parse_date(date_string):
    try:
        return datetime.strptime(date_string, '%d.%m.%Y')
    except ValueError:
        return None

def les_værdata(filnavn='snoedybdde.csv'):
    with open(filnavn, 'r') as file:
        next(file)
        værdata = []
        for linje in file:
            navn, stasjon, dato_str, snoedybde_str, nedbor_str, temp_str, skydekke_str, vind_str = linje.strip().split(';')
            dato = parse_date(dato_str)
            snoedybde = float_konvertering(snoedybde_str) if snoedybde_str not in ['-', ''] else None
            nedbor = float_konvertering(nedbor_str) if nedbor_str not in ['-', ''] else None
            temp = float_konvertering(temp_str) if temp_str not in ['-', ''] else None
            skydekke = float_konvertering(skydekke_str) if skydekke_str not in ['-', ''] else None
            vind = float_konvertering(vind_str) if vind_str not in ['-', ''] else None

            værdata.append({
                'Dato': dato,
                'snoedybde': snoedybde,
                'Nedbør': nedbor,
                'Middeltemperatur': temp,
                'Skydekke': skydekke,
                'vind': vind})
    return værdata

def antall_penværsdager(værdata):
    resultater = {}
    for data in værdata:
        dato = data['Dato']
        skydekke = data['Skydekke']

        if dato is not None:
            if dato.year not in resultater:
                resultater[dato.year] = 0

           
            if skydekke is not None and skydekke <= 3:
                resultater[dato.year] += 1

    return resultater

def plott_penværsdager(resultater):
    år = list(resultater.keys())
    antall_dager = list(resultater.values())

    plt.bar(år, antall_dager)
    plt.xlabel('År')
    plt.ylabel('Antall penværsdager')
    plt.title('Antall penværsdager for hvert år')
    plt.show()

if __name__ == "__main__":
    filnavn = 'snoedybdde.csv'  # Erstatt med riktig filnavn
    værdata = les_værdata(filnavn)
    resultater = antall_penværsdager(værdata)
    plott_penværsdager(resultater)
