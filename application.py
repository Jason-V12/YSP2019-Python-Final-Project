"""SpellChecker Main file - creates instances of classes and calls methods from 
helper files"""

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
