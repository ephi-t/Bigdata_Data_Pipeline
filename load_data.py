# load_data.py

import pandas as pd
from config import FILE_PATH

def load_data():
    """Load dataset from CSV file."""
    return pd.read_csv(FILE_PATH)

if __name__ == "__main__":
    df = load_data()
    print("Data Loaded Successfully!")
    print(df.head())
