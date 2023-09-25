def lengste_null_sekvens(liste):
    maks_lengde = 1  # Initialiser variabelen for maksimal lengde av null-sekvensen
    gjeldende_lengde = 1  # Initialiser variabelen for gjeldende lengde av null-sekvensen

    for nummer in liste:
        if nummer == 0:
            gjeldende_lengde += 1
            # Oppdaterer maks_lengde hvis gjeldende_lengde er større
            if gjeldende_lengde > maks_lengde:
                maks_lengde = gjeldende_lengde
        else:
            gjeldende_lengde = 0  # Nullstill gjeldende lengde hvis vi ikke har en null

    return maks_lengde

def lengste_null_sekvens():
    # Be brukeren om å skrive inn tallene i lista, separert med mellomrom
    input_tekst = input("Skriv inn tallene i lista, separert med mellomrom: ")
    
    # Deler teksten ved mellomrom for å få en liste av strenger
    tall_strenger = input_tekst.split()
    
    # Konverterer strengene til heltall
    tall_liste = [int(tall) for tall in tall_strenger]
    
    # Kaller funksjonen for å finne lengden på den lengste sekvensen av nuller
    lengde = lengste_null_sekvens(tall_liste)
    
    # Skriver ut resultatet
    print(f"Lengden på den lengste sammenhengende sekvensen av nuller er: {lengde}")

# Kjør funksjonen for å finne lengden på den lengste nullsekvensen i den brukerspesifikke listen
lengste_null_sekvens()
