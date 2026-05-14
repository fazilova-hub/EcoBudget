import pandas as pd
def load_data(file_path):
    """Загружает данные из CSV-файла."""
    df = pd.read_csv(file_path)
    return df
