# -*- coding: utf-8 -*-
import os
import pandas as pd

#Global Scope

iv_by_post = []
iv_by_fsc = []
niv_by_post = []
niv_by_nat = []

processed_directory = '../../data/processed'
consolidated_directory = '../../data/consolidated'

def scan_files():

    files = os.scandir(processed_directory)

    for fl in files:
        classify_file(fl.name)

def classify_file(fl_name):
    
    fl_name_split = fl_name.split(" - ")

    if fl_name_split[1].startswith("IV Issuances by FSC"):
        iv_by_fsc.append(fl_name)

    if fl_name_split[1].startswith("IV Issuances by Post"): 
        iv_by_post.append(fl_name)
    
    if fl_name_split[1].startswith("NIV Issuances by Nationality"):
        niv_by_nat.append(fl_name)

    if fl_name_split[1].startswith("NIV Issuances by Post"): 
        niv_by_post.append(fl_name)

def generate_panda_code(who, ln):

    res = f"iv = {ln}"

    res = f"""iv = pd.read_csv(
    ln,

    )"""

    return res

def generate_catalog(filename, list):

    full_filename = f"{processed_directory}/{filename}.txt"
    ln = ''

    fin = open(full_filename, "wt")

    for l in list:
        ln = generate_panda_code(filename, l)
        
        fin.write(f"{ln}\n")

    fin.close()

def consolidate_iv_by_post():
    print(f"📈 IV - by Post\n")

    frames = []

    for l in iv_by_post:

        month = l.split(' ')[0]
        year = l.split(' ')[1]

        fl = f"{processed_directory}/{l}"

        iv = pd.read_csv(
            fl,
            delimiter=',', 
            header=None,
            names=['Post', 'VisaClass', 'Quantity']
            )

        iv['VisaType'] = 'IV'
        iv['Year'] = year
        iv['Month'] = month

        frames.append(iv)

    res = pd.concat(frames, ignore_index=True)
    res.to_csv(f"{consolidated_directory}/iv_by_post.csv", index=False)

    print(res)

    #iterate files
    #base
    #generate dataframe
    #add
    #export


def consolidate_datasets():
    print(f"📊 Consolidate Datasets\n")

    consolidate_iv_by_post()

def print_summary():
    print(f"📋 File Catalog ")
    print(f"\t 📂 IV - by FSC {len(iv_by_fsc)}")
    print(f"\t 📂 IV - by Post {len(iv_by_post)}")
    print(f"\t 📂 NIV - by Nationality {len(niv_by_nat)}")
    print(f"\t 📂 NIV - by Post {len(niv_by_post)}")

def main():
    
    print("🔊 Generating Catalog \n")

    scan_files()
    consolidate_datasets()
    print_summary()

if __name__ == "__main__":
    main()