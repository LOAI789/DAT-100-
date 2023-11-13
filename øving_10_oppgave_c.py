"""

@author: rphin
"""

import numpy as np
import matplotlib.pyplot as plt

def calculate_trend(x, y):
    # Beregne gjennomsnitt av x og y
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # beregne  teller og nevner for stigningstall(a)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)

    # Beregne stigningstall (a) og skjæringspunktet i y (b)
    a = numerator / denominator
    b = y_mean - a * x_mean

    return a, b

# Skriv inn År og antall dager
years = np.array([int(input(f'skriv inn 6 år, år {i + 1}: ')) for i in range(6)])
days_skiing = np.array([int(input(f'skriv inn dager  {i + 1}: ')) for i in range(6)])

# Beregne trenden
slope, intercept = calculate_trend(years, days_skiing)

# Forutsi antall dager for hvert år ved å bruke trendlinjen
predicted_days = slope * years + intercept

# Plot de originale dataene og trendlinjen
plt.scatter(years, days_skiing, label='Faktiske data')
plt.plot(years, predicted_days, color='red', label='Trenden')
plt.xlabel('År')
plt.ylabel('Antall dager på ski')
plt.title('Skitrend gjennom årene')
plt.legend()
plt.show()

# Skriv ut det lineære trenduttrykket
print(f'Lineær likning er : y = {slope:.2f} * x + {intercept:.2f}')
