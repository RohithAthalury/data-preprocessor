
### `process_csv.py`

```python
import pandas as pd
import sys

def process_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
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
        print("\nNo numeric columns found in the CSV file.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_csv.py path/to/yourfile.csv")
    else:
        process_csv(sys.argv[1])
