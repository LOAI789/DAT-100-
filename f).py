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
    with open(filnavn, 'r', encoding='utf-8') as file:
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
                'vind': vind
            })
    return værdata


def finn_lengste_tørkeperiode(værdata):
    tørke_perioder = {}
    nåværende_tørke_start = None
    nåværende_tørke_lengde = 0

    for data in værdata:
        dato = data['Dato'] #henter datoene 
        nedbør = data['Nedbør'] #henter nedbør

        if nedbør is None or nedbør == 0:
            nåværende_tørke_lengde += 1 #hvis nedbør er null øk med 1

            if nåværende_tørke_start is None:
                nåværende_tørke_start = dato
        else:
            if nåværende_tørke_start is not None: # sjekke om det er tørkeperioder
                år = dato.year
                if år not in tørke_perioder:
                    tørke_perioder[år] = {'start': nåværende_tørke_start, 'lengde': nåværende_tørke_lengde} # legger til år i en liste ("tørke_perioder") 
                else:
                    # betyr at det finnes allerede
                    if nåværende_tørke_lengde > tørke_perioder[år]['lengde']: #sjekker om det allerede eksisterende periode er større/lengre enn perioden for dette året
                        tørke_perioder[år] = {'start': nåværende_tørke_start, 'lengde': nåværende_tørke_lengde}

                nåværende_tørke_start = None
                nåværende_tørke_lengde = 0

    år = list(tørke_perioder.keys())
    lengder = [tørke_perioder[år]['lengde'] for år in år]

    plt.bar(år, lengder)
    plt.xlabel('År')
    plt.ylabel('Lengden av tørkeperiode (dager)')
    plt.title('Lengste tørkeperiode hvert år')
    plt.show()

    return tørke_perioder


værdata = les_værdata()
tørke_perioder = finn_lengste_tørkeperiode(værdata)
