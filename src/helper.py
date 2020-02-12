# -*- coding: utf-8 -*-
import os

def count_files(dir):
    return len([1 for x in list(os.scandir(dir)) if x.is_file()])

def file_remove_str(filename, list_strings):

    fin = open(filename, "rt")
    data = fin.read()
    data = data.lower()

    for strng in list_strings:
        #print(strng)
        data = data.replace(strng.lower(), '')
 
    fin.close()

    fin = open(filename, "wt")
    fin.write(data)
    fin.close()

def clean_working_dir(directory):
    files = os.scandir(directory)
    
    for f in files:
        os.remove(f)

def file_remove_ln(filename, list_strings):

    fin = open(filename, "rt")
    data = fin.read()

    for ln in data.splitlines():
        for strng in list_strings:
            if ln.strip().startswith(strng.lower()):
                data = data.replace(ln, '')
    
    fin.close()

    fin = open(filename, "wt")
    fin.write(data)
    fin.close()

def file_remove_empty_lines(fl):
    fh = open(fl, "r")
    lines = fh.readlines()
    fh.close()

    # Weed out blank lines with filter
    lines = filter(lambda x: not x.isspace(), lines)
    
    # Write
    fh = open(fl, "w")
    fh.write("".join(lines))
    # should also work instead of joining the list:
    # fh.writelines(lines)

    fh.close()
