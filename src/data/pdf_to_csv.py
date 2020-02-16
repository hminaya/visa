# -*- coding: utf-8 -*-
import tabula as tb
import os

import sys
sys.path.append('../')

import helper

# Global Scope
raw_directory = '../../data/raw'
csv_directory = '../../data/interim'

def clean_working_dir():
    print('💀 Cleaning up working directory')
    helper.clean_working_dir(csv_directory)

def convert_pdf_into_csv():
    print(f'📂 Converting PDF files - {helper.count_files(raw_directory)}')

    files = os.scandir(raw_directory)
    i = 0

    for entry in files:
        
        if (entry.path.endswith(".pdf")) and entry.is_file():
            i= i + 1

            # File Path
            fl = entry.path

            tb.convert_into(fl, fl.replace("pdf", "csv").replace("raw", "interim"), output_format="csv", pages='all')

            print(f'\t ✔ {i} - {fl.replace(f"{raw_directory}/","")} 👉 {fl.replace(f"{raw_directory}/","").replace("pdf","csv")} ')

def main():

    print("🔊 Convert Raw PDF Files into CSV \n")

    clean_working_dir()
    convert_pdf_into_csv()

    print("✅ Done \n")

if __name__ == "__main__":
    main()