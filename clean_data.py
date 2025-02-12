# clean_data.py

import pandas as pd

def clean_data(df):
    """Clean the dataset: handle missing values, remove duplicates, standardize text columns."""
    
    # Handle Missing Values
    df["days_since_prior_order"] = df["days_since_prior_order"].fillna(0).astype(int)

    # Remove Duplicate Rows
    df = df.drop_duplicates()

    # Ensure Correct Data Types
    df["order_dow"] = df["order_dow"].astype(int)
    df["order_hour_of_day"] = df["order_hour_of_day"].astype(int)

    # Standardize Text Columns
    df["department"] = df["department"].str.lower().str.strip()
    df["product_name"] = df["product_name"].str.lower().str.strip()

    return df

if __name__ == "__main__":
    from load_data import load_data

    df = load_data()
    df = clean_data(df)
    print("Data Cleaned Successfully!")
    print(df.head())
