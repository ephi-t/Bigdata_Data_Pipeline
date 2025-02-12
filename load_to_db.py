# load_to_db.py

import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, CLEANED_FILE_PATH

def load_data_to_postgresql():
    """Load cleaned data into PostgreSQL database."""
    
    # Create database connection
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    
    # Load cleaned data
    df = pd.read_csv(CLEANED_FILE_PATH)
    
    # Insert data into table
    df.to_sql("orders", engine, if_exists="append", index=False)
    
    print("\nData successfully inserted into PostgreSQL!")

if __name__ == "__main__":
    load_data_to_postgresql()
