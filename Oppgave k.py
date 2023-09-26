"""

@author: rphin
"""
# beregne trenden this x og y
def calculate_trend(x, y):
    # sjekke om listene har samme lengde
    if len(x) != len(y):
        raise ValueError("Feil, listene må ha samme lengde")
    
    # bergene gjennomsnitten
    x_bar = sum(x) / len(x)
    y_bar = sum(y) / len(x)
    
    # beregne a og b
    teller_a = sum((xi - x_bar) * (yi - y_bar) for xi, yi in zip(x, y))
    nevner_a = sum((xi - x_bar) ** 2 for xi in x)
    a = teller_a / nevner_a
    b = y_bar - a * x_bar
    
    return a, b

# temperatur data
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
temperaturer_tidspunkter = list(range(len(temperaturer)))

# beregne trenden
a, b = calculate_trend(temperaturer_tidspunkter, temperaturer)

if a > 0:
    posisjon = "er sigende"
elif a < 0:
    posisjon = "er synkende"
else:
    posisjon = "finnes ikke"

# skriver ut resultatet
print(f"Trenden {posisjon}.")
print(f"a = {a}, b = {b}")
