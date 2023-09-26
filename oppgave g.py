"""

@author: rphin
"""
#den beregner trenden this x og y
def calculate_trend(x, y):
    # sjekke om listene har samme lengde
    if len(x) != len(y):
        raise ValueError("Feil, listene må ha samme lengde")

    # bergene gjennomsnitten
    x_bar = sum(x) / len(x)
    y_bar = sum(y) / len(y)

    # beregne a og b ved hjelp av de oppgitte formlene
    teller_a = sum((xi - x_bar) * (yi - y_bar) for xi, yi in zip(x, y))
    nevner_a = sum((xi - x_bar) ** 2 for xi in x)

    a = teller_a / nevner_a
    b = y_bar - a * x_bar

    return a, b

# skriv inn verider til x og y
x_verdier = input("Skriv inn x-listen som kommadelte verdier: ")
y_verdier = input("Skriv inn y-listen som kommadelte verdier: ")

x_verdier = [float(x) for x in x_verdier.split(",")]
y_verdier = [float(y) for y in y_verdier.split(",")]

a, b = calculate_trend(x_verdier, y_verdier)

print(f"Lineær likning er y = {a}x + {b}")


