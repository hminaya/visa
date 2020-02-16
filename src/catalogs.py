# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np

iv_catalog = '../../data/catalog/iv_symbols.csv'
niv_catalog = '../../data/catalog/niv_symbols.csv'

def visa_class_catalog():

    iv = pd.read_csv(iv_catalog, delimiter="|")
    niv = pd.read_csv(niv_catalog, delimiter="|")

    frames = []

    frames.append(iv)
    frames.append(niv)

    res = pd.concat(frames, ignore_index=True)

    res = res.VisaClass.str.lower().str.replace('-', '', regex=False).str.strip().unique()

    return res

def iv_class_catalog():
    
    iv = pd.read_csv(iv_catalog, delimiter="|")

    iv['VisaClass'] = iv['VisaClass'].str.lower()

    return iv

def niv_class_catalog():
    niv = pd.read_csv(niv_catalog, delimiter="|")

    niv['VisaClass'] = niv['VisaClass'].str.lower().str.replace('-', '', regex=False)
    niv['Category'] = 'NIV'
    niv['SubCategory'] = 'NIV'

    return niv

def iv_class():
    
    iv = pd.read_csv(iv_catalog, delimiter="|")

    res = iv.VisaClass.str.lower().str.strip().unique()

    return res

def niv_class():
    
    niv = pd.read_csv(niv_catalog, delimiter="|")

    res = niv.VisaClass.str.lower().str.strip().unique()

    return res
