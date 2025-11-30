"""
Funzioni per caricare dati
Utilizzabile da tutti i notebook
"""

import pandas as pd
import warnings
from . import config

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

def load_all_csv():
    """Carica tutti i file CSV"""
    
    data = {}
    
    print("📥 Caricamento CSV files...")
    
    csv_files = {
        'df_regioni_base': config.FILES['regioni_base'],
        'delitti_2018': config.FILES['delitti_2018'],
        'delitti_2019': config.FILES['delitti_2019'],
        'delitti_2020': config.FILES['delitti_2020'],
        'popolazione': config.FILES['popolazione'],
        'risorse_umane': config.FILES['risorse_umane'],
        'posas_province': config.FILES['posas_province'],
        'posas_comuni': config.FILES['posas_comuni'],
        'posas_regioni': config.FILES['posas_regioni'],
        'posas_ripartizioni': config.FILES['posas_ripartizioni'],
        'estat': config.FILES['estat'],
    }
    
    # CSV speciali con encoding
    special_csv = {
        'spese_consolidate': (config.FILES['spese_consolidate'], 'latin1', ';'),
        'spese_stato': (config.FILES['spese_stato'], 'latin1', ';'),
        'spese_enti': (config.FILES['spese_enti'], 'latin1', ';'),
    }
    
    # Carica CSV normali
    for name, filename in csv_files.items():
        try:
            data[name] = pd.read_csv(config.get_raw_path(filename))
            print(f"  ✅ {name}: {data[name].shape}")
        except FileNotFoundError:
            print(f"  ❌ {name}: File non trovato")
    
    # Carica CSV speciali
    for name, (filename, encoding, sep) in special_csv.items():
        try:
            data[name] = pd.read_csv(
                config.get_raw_path(filename),
                encoding=encoding,
                sep=sep
            )
            print(f"  ✅ {name}: {data[name].shape}")
        except FileNotFoundError:
            print(f"  ❌ {name}: File non trovato")
    
    return data


def load_all_excel():
    """Carica tutti i file Excel"""
    
    data = {}
    
    print("\n📊 Caricamento Excel files...")
    
    excel_files = {
        'delitti_2016_xl': config.FILES['delitti_2016_xl'],
        'delitti_2017_xl': config.FILES['delitti_2017_xl'],
        'delitti_2021_xl': config.FILES['delitti_2021_xl'],
        'delitti_2022_xl': config.FILES['delitti_2022_xl'],
        'delitti_2023_xl': config.FILES['delitti_2023_xl'],
    }
    
    for name, filename in excel_files.items():
        try:
            data[name] = pd.read_excel(config.get_raw_path(filename))
            print(f"  ✅ {name}: {data[name].shape}")
        except FileNotFoundError:
            print(f"  ❌ {name}: File non trovato")
    
    return data


def load_all_data():
    """Carica tutti i dati (CSV + Excel)"""
    
    print("="*60)
    print("🔧 CARICAMENTO DATI")
    print("="*60)
    
    csv_data = load_all_csv()
    excel_data = load_all_excel()
    
    all_data = {**csv_data, **excel_data}
    
    print("\n" + "="*60)
    print(f"✅ Caricati {len(all_data)} dataset")
    print("="*60)
    
    return all_data