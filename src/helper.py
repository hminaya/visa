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

def file_transform_lines(filename, list_strings):
    fin = open(filename, "rt")
    data = fin.read()
    data = data.lower()

    for strng in list_strings:
        #print(strng)
        data = data.replace(strng[0].lower(), strng[1].lower())
 
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

def file_add_commas(filename, valid_visa_types):
    fin = open(filename, "rt")
    data = fin.read()
    
    #New Line
    data_new = ''

    #Columns
    quantity = ''
    visa_class = ''
    post = ''

    #Split file into lines
    for ln in data.splitlines():

        if len(ln) > 0:
            #Split into columns
            ln_new = ln.split(" ")
            
            #for each column
            for w in ln_new:

                if w in valid_visa_types:

                    quantity = ''
                    visa_class = ''
                    post = ''

                    loc_class = ln_new.index(w)
                    loc_end = len(ln_new)

                    visa_class = w

                    # Everything to the right is the Quantity
                    for x in range(loc_class+1, loc_end):
                        quantity = f"{quantity}" + f"{ln_new[x]}"
                        quantity = quantity.strip()

                    # Everything to the left is the Post
                    for x in range(0, loc_class):
                        post = f"{post} " + f"{ln_new[x]}"
                        post = post.strip()

            ln_new = f"{post}, {visa_class}, {quantity}\n"
            data_new = f"{data_new}" + ln_new
 
    fin.close()

    fin = open(filename, "wt")
    fin.write(data_new)
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
