# main.py

from load_data import load_data
from clean_data import clean_data
from save_data import save_cleaned_data
from db_setup import create_postgresql_table
from load_to_db import load_data_to_postgresql

def main():
    """Main function to execute the entire data pipeline."""
    
    # Load raw data
    df = load_data()

    # Clean data
    df = clean_data(df)

    # Save cleaned data
    save_cleaned_data(df)

    # Setup database table
    create_postgresql_table()

    # Load cleaned data into PostgreSQL
    load_data_to_postgresql()

if __name__ == "__main__":
    main()
