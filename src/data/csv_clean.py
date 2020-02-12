# -*- coding: utf-8 -*-
import os

from shutil import copyfile

import sys
sys.path.append('../')

import helper

# Global Scope
interim_directory = '../../data/interim'
processed_directory = '../../data/processed'

unwanted_strings = [
    ' - ',
    '"',
    'Nonimmigrant Visa Issuances by Nationality',
    'Nonimmigrant Visa Issuances by Post',
    'Immigrant Visa Issuances By Post',
    'Immigrant Visa Issuances',
    'By Foreign State of Chargeability',
    'Foreign State of Chargeability or',
    'or Place of Birth',
    'Nationality Visa Class Issuances',
    'Post Visa Class Issuances',
    'Place of Birth,Visa Class,Issuances',
    'Post,Visa Class,Issuances',
    'Place of Birth Visa Class Issuances',
    'foreign state of chargeability',
    'visa class issuances',
    ',visa class,issuances',
    ',,'
]
unwanted_lines = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August', 
    'September', 'October', 'November', 'December',
    '(fy ',
    'grand total'
]
transform_strings = [
    ['bahamas, the', 'the bahamas'],
    ['congo, democratic republic of the', 'democratic republic of the congo'],
    ['congo, republic of the', 'republic of the congo'],
    ['gambia, the', 'the gambia'],
    ['korea, north', 'north korea'],
    ['korea, south', 'south korea'],
    ['micronesia, federated states of', 'federated states of micronesia'],
]

def clean_working_dir():
    print('💀 Cleaning up working directory')
    helper.clean_working_dir(processed_directory)

def copy_interim_files():
    print('📋 Copy files to working directory')

    files = os.scandir(interim_directory)

    for f in files:
        fl = f.path
        copyfile(fl, fl.replace(interim_directory,processed_directory))

def clean_up_file(fl):
    print(f'\t {fl.path.replace(f"{processed_directory}/","")}')

    # Remove Titles/Strings
    helper.file_remove_str(fl.path, unwanted_strings)

    # Remove Lines
    helper.file_remove_ln(fl.path, unwanted_lines)

    # Remove empty lines
    helper.file_remove_empty_lines(fl.path)

    # Transform lines
    helper.file_transform_lines(fl.path, transform_strings)

def clean_up_data():
    print('🧹 Cleaning up data inside files')

    files = os.scandir(processed_directory)

    for f in files:
        clean_up_file(f)

def main():

    print("🔊 Cleaning up CSV Files \n")

    clean_working_dir()
    copy_interim_files()
    clean_up_data()

    print("✅ Done \n")

if __name__ == "__main__":
    main()