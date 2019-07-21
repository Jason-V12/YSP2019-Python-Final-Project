"""SpellChecker Main file - creates instances of classes and calls methods from 
helper files"""

import trie
import interface
from string import punctuation
from time import time


# @param {}
# @return {string} dictionary if successful, else {boolean} False
# Reads in dictionary requested from user input
def read_dict():
    # TODO: handle different dictionaries via options in interface.py
    language = interface_instance.language
    if language == "English":
        dictionary_option = "EnglishDictionary.txt"
    else:
        dictionary_option = "EnglishDictionary.txt"
    dictionary_option = dict_file = open(dictionary_option, "r")
    dict_in = dict_file.read()
    if dict_in == "":
        return False
    else:
        return dict_in


# @param {}
# @return {string} input_file if successful, else {boolean} False
# Reads in file from file location specified by user, converts file to .txt if applicable
def get_file():
    # TODO: Get file location from user via text field in interface.py
    print(interface_instance.file_location)
    if interface_instance.file_location:
        dot_index = interface_instance.file_location.rfind(".")
        file_type = interface_instance.file_location[dot_index:]
        print("File type: " + file_type)
        if file_type == ".txt":
            file_in = open(interface_instance.file_location, 'r')
            in_file = file_in.read()
            file_in.close()
            # output_file = open("READ_IN.txt", "w")
            # output_file.write(in_file)
            # output_file.close()
            return in_file
        else:
            print("Please use a valid file type")
            return False
    else:
        print("File not obtained")
        exit(4)
    # TODO: Convert file to .txt if not already
    # TODO: Read in file to variable file_in
    # TODO: Return file_in if successful, else return False


if __name__ == "__main__":
    complete_time = time()
    interface_instance = interface.DrawInterface()
    interface_instance.make_interface()
    print(interface_instance.language)
    print("Select a file to process, then select exit...\n")
    try:
        interface_instance.top.mainloop()
    except AttributeError:
        exit(1)
    input_file = get_file()
    print("Loading...")
    input_file = input_file.replace("\n", " ")
    input_file = input_file.replace("\t", " ")
    input_file = (input_file.translate(str.maketrans('', '', punctuation))).split(" ")
    if not input_file:
        exit(3)
    dictionary = read_dict()
    trie_instance = trie.Trie(dictionary)
    if not trie_instance.check_dict():
        exit(2)
    else:
        trie_instance.add_words()
    spell_check_time = time()
    miss_file = open("MisspelledWords.txt", "w")
    for word in range(0, len(input_file)):
        if input_file[word] != "" and not input_file[word].isnumeric():
            result = trie_instance.check_word(input_file[word])
            if not result:
                miss_file.write(input_file[word] + ": " + str(result) + "   Similar: "
                                + str(trie_instance.suggestions(input_file[word])) + "\n")
    print("Spell Checking time in seconds: " + str(time() - spell_check_time))
    miss_file.close()
    print("Completed runtime in seconds: " + str(time() - complete_time))
    print("SUCCESS")
    print("Misspelled words located in file: MisspelledWords.txt")

"""elif file_type == "pdf":
        newFile = textract.process(fileLocation, method = "pdfminer")
        file_in = file_in(newFile, 'r')
    elif file_type == "doc":
        newFile = textract.process(fileLocation, method = "antiword")
        file_in = file_in(newFile, 'r')"""
