import tabula
import os
import pandas as pd

pdf_folder = 'C:/Users/macis/Desktop/yarrrml/pdf_regione/'
all_pdf_files = os.listdir(pdf_folder)

for pdf_path in all_pdf_files:
    csv_path = pdf_path.replace('.pdf', '.csv')
    tabula.convert_into(pdf_folder + pdf_path, pdf_folder + csv_path, output_format="csv", pages='all')
