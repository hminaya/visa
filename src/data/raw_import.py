# -*- coding: utf-8 -*-
import mechanize
import os
from time import sleep

# Browser Info http://stockrt.github.com/p/emulating-a-browser-in-python-with-mechanize/

# Global Scope
br = mechanize.Browser()

filetypes=[".pdf"] 
iv_link = 'https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics/immigrant-visa-statistics/monthly-immigrant-visa-issuances.html'
niv_link = 'https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics/nonimmigrant-visa-statistics/monthly-nonimmigrant-visa-issuances.html'

raw_directory = '../../data/raw/'
removeFiles=["click here.pdf"]
myfiles=[]

def get_links(url):
    
    br.open(url)

    for l in br.links(): 
        for t in filetypes:
            if t in str(l): 
                myfiles.append(l)

def download_files():
    print(f'📂 Starting to download files ({len(myfiles)})')
    
    i = 0

    for l in myfiles:
        i= i + 1
        sleep(1) #throttle so you dont hammer the site
        
        br.retrieve(f'https://travel.state.gov{l.url}', f'{raw_directory}{l.text}.pdf')[0]
        print(f'\t ✔ {i} - {l.url}')

    print('Finished downloading files......')

def clean_working_dir():
    print('💀 Cleaning up working directory')

    files = os.scandir(raw_directory)
    
    for f in files:
        os.remove(f)

def clean_up_files():
    print('🧹 Cleaning up working directory')
    helper.clean_working_dir(raw_directory)

def main():
    
    print("🔊 Import Raw PDF Files \n")

    clean_working_dir()
    get_links(iv_link)
    get_links(niv_link)
    download_files()
    clean_up_files()

    print("✅ Done \n")

if __name__ == "__main__":
    main()