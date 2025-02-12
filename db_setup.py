# db_setup.py

import psycopg2
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

def create_postgresql_table():
    """Create the 'orders' table in PostgreSQL if it does not exist."""
    
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT PRIMARY KEY,
        user_id INT,
        order_number INT,
        order_dow INT,
        order_hour_of_day INT,
        days_since_prior_order INT,
        product_id INT,
        add_to_cart_order INT,
        reordered INT,
        department_id INT,
        department VARCHAR(50),
        product_name VARCHAR(255)
    );
    """
    
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()
    print("\nTable 'orders' created successfully.")

if __name__ == "__main__":
    create_postgresql_table()
