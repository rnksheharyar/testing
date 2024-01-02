import pdfplumber
import pandas as pd

def parse_pdf_to_excel(pdf_path, excel_path):
    # Open the PDF with pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        # Initialize a list to store the tables
        tables = []

        # Iterate through the pages of the PDF
        for page in pdf.pages:
            # Extract tables from the page
            for table in page.extract_tables():
                # Convert the table to a DataFrame and add it to 'tables'
                tables.append(pd.DataFrame(table))

        # Concatenate all tables into a single DataFrame
        tables = pd.concat(tables)

    # Write the tables to an Excel file
    tables.to_excel(excel_path, index=False)

if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your PDF file
    pdf_path = 'python面试题_测试文档.pdf'
    
    # Replace 'output.xlsx' with the desired Excel file name
    excel_path = 'new.xlsx'
    
    parse_pdf_to_excel(pdf_path, excel_path)