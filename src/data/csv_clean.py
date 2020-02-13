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
    'grand total',
    'post'
]
transform_strings = [
    ['bahamas, the', 'the bahamas'],
    ['congo, democratic republic of the', 'democratic republic of the congo'],
    ['congo, republic of the', 'republic of the congo'],
    ['gambia, the', 'the gambia'],
    ['korea, north', 'north korea'],
    ['korea, south', 'south korea'],
    ['micronesia, federated states of', 'federated states of micronesia'],
    ['micronesia, federated states of', 'federated states of micronesia'],
    [',', ' '],
    ['  ', ' ']
]

valid_visa_types = [
        'cr1', 'dv1', 'f11', 'f21', 'f22', 'f24', 'fx1', 'fx2',
       'ir1', 'ir2', 'ir5', 'sb1', 'se1', 'se2', 'cr2', 'dv2',
       'dv3', 'e22', 'e23', 'e31', 'e34', 'e35', 'f12', 'f31',
       'f32', 'f33', 'f41', 'f42', 'f43', 'fx3', 'sq2', 'f23',
       'f25', 'ib2', 'ib3', 'iw1', 'e21', 'se3', 'e32', 'i51',
       'i52', 'i53', 't51', 't52', 'ir4', 'e14', 'sq1', 'sq3',
       'ib1', 'ew3', 'ew4', 'ew5', 'ih3', 'ih4', 'e11', 'ir3',
       'e15', 'sd1', 'iw2', 'bx1', 'su3', 'c51', 'c52',
       'c53', 'e13', 't53', 'am1', 'am2', 'si1', 'si2', 'si3',
       'sr1', 'sr2', 'sr3', 'sd2', 'sd3', 'bc1'
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

    # Transform lines
    helper.file_transform_lines(fl.path, transform_strings)

    # Remove Titles/Strings
    helper.file_remove_str(fl.path, unwanted_strings)

    # Remove Lines
    helper.file_remove_ln(fl.path, unwanted_lines)

    # Remove empty lines
    helper.file_remove_empty_lines(fl.path)

    # Add commas
    helper.file_add_commas(fl.path, valid_visa_types)

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