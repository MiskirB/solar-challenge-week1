import pandas as pd

def load_data():
    benin = pd.read_csv("data/benin-malanville.csv", parse_dates=['Timestamp'])
    sierraleone = pd.read_csv("data/sierraleone-bumbuna.csv", parse_dates=['Timestamp'])
    togo = pd.read_csv("data/togo-dapaong_qc.csv", parse_dates=['Timestamp'])

    benin['Country'] = 'Benin'
    sierraleone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    combined = pd.concat([benin, sierraleone, togo], ignore_index=True)
    return combined
