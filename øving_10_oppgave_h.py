"""

@author: rphin
"""

import pandas as pd
import matplotlib.pyplot as plt
file_path = 'snoedybder_vaer_en_stasjon_dogn.csv'

# Funksjon for å lese og behandle CSV-file
def process_csv(file_path):
    # Les CSV-filen med pandaer
    df = pd.read_csv(file_path, sep=';', parse_dates=['Tid(norsk normaltid)'], dayfirst=True)

    # Filtrer ut rader med manglende vinddata
    df = df.dropna(subset=['Høyeste middelvind (døgn)'])

    # Konverter vinddata til numeriske
    df['Høyeste middelvind (døgn)'] = pd.to_numeric(df['Høyeste middelvind (døgn)'], errors='coerce')

    # Filtrer ut år med mindre enn 300 dager med vinddata
    valid_years = df.groupby(df['Tid(norsk normaltid)'].dt.year).filter(lambda x: len(x) >= 300)

    return valid_years

# Funksjon for å plotte høyeste middelvind og median vindstyrke for hvert år
def plot_wind_statistics(data):
    # Grupper data etter år
    grouped_data = data.groupby(data['Tid(norsk normaltid)'].dt.year)

    # Beregn gjennomsnittlig og median vindstyrke for hvert år
    mean_wind = grouped_data['Høyeste middelvind (døgn)'].mean()
    median_wind = grouped_data['Høyeste middelvind (døgn)'].median()

    # Plott resultatene
    plt.figure(figsize=(10, 6))
    plt.plot(mean_wind.index, mean_wind, label='Høyeste middelvind ')
    plt.plot(median_wind.index, median_wind, label='Medianen for vindstyrke', linestyle='dashed')
    plt.xlabel('År')
    plt.ylabel('Vindstyrke')
    plt.title('Høyeste middelvind og medianen for vindstyrke for hvert år ')
    plt.legend()
    plt.show()



# Behandle CSV-filen og plott vindstatistikk
data = process_csv(file_path)
plot_wind_statistics(data)
