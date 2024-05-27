import pandas as pd
import sqlite3
import sys

def process_sql(db_path, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Read the table into a DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    
    # Display basic information about the data
    print("Data Overview:")
    print(df.info())
    print("\nFirst 5 Rows:")
    print(df.head())
    
    # Calculate and display statistics for numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    if not numeric_cols.empty:
        print("\nStatistics for Numeric Columns:")
        for col in numeric_cols:
            print(f"\nColumn: {col}")
            print(f"Mean: {df[col].mean()}")
            print(f"Median: {df[col].median()}")
            print(f"Mode: {df[col].mode().values}")
    else:
        print("\nNo numeric columns found in the SQL table.")
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_sql.py path/to/yourdatabase.db tablename")
    else:
        process_sql(sys.argv[1], sys.argv[2])
