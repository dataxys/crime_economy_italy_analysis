"""
Configurazione path del progetto
Funziona per tutti i membri del team indipendentemente dalla posizione locale
"""

import os
from pathlib import Path

# Root del progetto (dove sta .git)
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

# Path dati
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'

# Path output
OUTPUT_DIR = PROJECT_ROOT / 'output'
VIZ_DIR = PROJECT_ROOT / 'visualizations'

# Crea cartelle se non esistono
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, OUTPUT_DIR, VIZ_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# File paths (nomi file)
FILES = {
    # CSV
    'delitti_2018': 'delitti_2018.csv',
    'delitti_2019': 'delitti_2019.csv',
    'delitti_2020': 'delitti_2020.csv',
    'popolazione': 'popolazione_media_annua.csv',
    'risorse_umane': 'risorse_umane_2018-2022.csv',
    'spese_consolidate': '2023-Territorio-destinatario-finale-della-spesa-consolidata.csv',
    'spese_stato': '2023-Distribuzione-territoriale-della-spesa-Stato.csv',
    'spese_enti': '2023-Distribuzione-territoriale-della-spesa-Enti.csv',
    'posas_province': 'POSAS_2025_it_Province.csv',
    'posas_comuni': 'POSAS_2025_it_Comuni.csv',
    'posas_regioni': 'POSAS_2025_it_Regioni.csv',
    'posas_ripartizioni': 'POSAS_2025_it_Ripartizioni.csv',
    'estat': 'estat_sdg_08_10_en.csv',
    'regioni_base': 'ita_reg_ann_data.csv',
    
    # Excel
    'delitti_2016_xl': 'INT00062 Delitti denunciati dati 2016.xlsx',
    'delitti_2017_xl': 'INT00062 Delitti denunciati  - dati anno 2017 - dati Nazionali, Regionali, Provinciali.xlsx',
    'delitti_2021_xl': 'INT00062_Delitti_denunciati_2021_ITA-REG-PROV-CP.xlsx',
    'delitti_2022_xl': 'INT00062_Delitti_denunciati_2022_ITA-REG-PROV-CP.xlsx',
    'delitti_2023_xl': 'INT00062_Delitti_denunciati_2023_ITA-REG-PROV-CP.xlsx',
}

def get_raw_path(filename):
    """Ritorna path completo per file raw"""
    return RAW_DATA_DIR / filename

def get_processed_path(filename):
    """Ritorna path completo per file processato"""
    return PROCESSED_DATA_DIR / filename

# Stampa info (per debug)
if __name__ == "__main__":
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Raw Data: {RAW_DATA_DIR}")
    print(f"Processed Data: {PROCESSED_DATA_DIR}")