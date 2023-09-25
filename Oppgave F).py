def lengste_null_sekvens(liste):
    maks_lengde = 0 
    gjeldende_lengde = 0 

    for nummer in liste:
        if nummer == 0:
            gjeldende_lengde += 1
            if gjeldende_lengde > maks_lengde:
                maks_lengde = gjeldende_lengde
        else:
            gjeldende_lengde = 0 

    return maks_lengde

døgn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]


resultat = lengste_null_sekvens(døgn_nedbor)

# Skriv ut resultatet
print(f"Lengden på den lengste perioden uten nedbør er: {resultat}")
