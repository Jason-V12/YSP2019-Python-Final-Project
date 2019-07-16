"""SpellChecker Main file - creates instances of classes and calls methods from 
helper files"""

import textract
from node import *
from interface import *

# @param {}
# @return {string} dictionary if successful, else {boolean} False
# Reads in dictionary requested from user input
def read_dict()
    # TODO: handle different dictionaries via options in interface.py
    dict_file = open("EnglishDictionary.txt", "r")
    dict_in = dict_file.read()
    if dict_in == "":
        return False
    else:
        return dict_in

# @param {}
# @return {string} file if successful, else {boolean} False
# Reads in file from file location specified by user, converts file to .txt if applicable
# @param {fileLocation}
# @return {string} file if successful, else {boolean} False
# Reads in file from file location specified by user, converts file to .txt if applicable
def get_file(fileLocation)
    # TODO: Get file location from user via text field in interface.py
    # TODO: Redirect back to interface if file not found/not in correct format (.txt, .pdf, .word)
    dotIndex = fileLocation.rfind(".")
    fileType = fileLocation[dotIndex:]
    if fileType == "txt":
        file_in = file(fileLocation, 'r')
    elif fileType == "pdf":
        newFile = textract.process(fileLocation, method = "pdfminer")
        file_in = file(newFile, 'r')
    elif fileType == "doc":
        newFile = textract.process(fileLocation, method = "antiword")
        file_in = file(newFile, 'r')
    else:
        print("Please use a valid file type")
    # TODO: Convert file to .txt if not already
    # TODO: Read in file to variable file_in
    file_in = file(newFile, 'r')
    if file_in.read() == "":
        return False
    else:
        return True
    # TODO: Return file_in if successful, else return False

# @param {string} dictionary
# @return {boolean} success_value
# Loads dictionary into memory, uses node objects to construct complete trie
def trie(dictionary):

if __name__ == "__main__":
    dictionary = read_dict()
    if not dictionary:
        exit(1)
    else:
        trie(dictionary)
print("Completed runtime")
