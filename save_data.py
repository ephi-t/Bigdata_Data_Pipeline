# save_data.py

import pandas as pd
from config import CLEANED_FILE_PATH

def save_cleaned_data(df):
    """Save cleaned data to CSV file."""
    df.to_csv(CLEANED_FILE_PATH, index=False)
    print(f"Cleaned data saved as '{CLEANED_FILE_PATH}'")

if __name__ == "__main__":
    from clean_data import clean_data
    from load_data import load_data

    df = load_data()
    df = clean_data(df)
    save_cleaned_data(df)
