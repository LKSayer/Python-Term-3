
import pandas as pd

import openpyxl


def read_excel_file(file_path):

    try:

        # Read the Excel file using pandas

        df = pd.read_excel(file_path)

        column = df['BirthWeight']

 

        # Print the entire DataFrame

        print("Data in the Excel file:")

        print(column)

 

    except FileNotFoundError:

        print(f"File not found at path: {file_path}")

    except pd.errors.ParserError:

        print(f"Error parsing the file at path: {file_path}")

if __name__ == "__main__":

    file_path = r"C:\Users\Liam\OneDrive\Documents\Snake\.venv\BirthWeight.xlsx"

    read_excel_file(file_path)