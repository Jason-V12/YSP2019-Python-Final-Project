"""SpellChecker Main file - creates instances of classes and calls methods from 
helper files"""

import trie
import interface
from string import punctuation


# @param {}
# @return {string} dictionary if successful, else {boolean} False
# Reads in dictionary requested from user input
def read_dict():
    # TODO: handle different dictionaries via options in interface.py
    dictionary_option = "EnglishDictionary.txt"
    dict_file = open(dictionary_option, "r")
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
        print(file_type)
        if file_type == ".txt":
            file_in = open(interface_instance.file_location, 'r')
            in_file = file_in.read()
            file_in.close()
            output_file = open("READ_IN.txt", "w")
            output_file.write(in_file)
            output_file.close()
            return in_file
        else:
            print("Please use a valid file type")
            return False
    else:
        print("File not obtained")
    # TODO: Convert file to .txt if not already
    # TODO: Read in file to variable file_in
    # TODO: Return file_in if successful, else return False


# @param {string} dictionary
# @return {boolean} success_value
# Loads dictionary into memory, uses node objects to construct complete trie
if __name__ == "__main__":
    interface_instance = interface.DrawInterface()
    interface_instance.make_interface()
    try:
        interface_instance.top.mainloop()
    except AttributeError:
        exit(1)
    input_file = get_file()
    input_file = (input_file.translate(str.maketrans('', '', punctuation))).split(" ")
    i = 0
    length = len(input_file)
    while i < length:
        input_file[i] = input_file[i].replace("\n", "")
        if input_file[i] == "":
            input_file.remove(input_file[i])
            length = length - 1
            continue
        i = i + 1
    if not input_file:
        exit(3)
    dictionary = read_dict()
    trie_instance = trie.Trie(dictionary)
    if not trie_instance.check_dict():
        exit(2)
    else:
        print(trie_instance.add_words())
    for word in range(0, len(input_file)):
        print(input_file[word] + ": " + str(trie_instance.check_word(input_file[word])))
    print(input_file)
print("Completed runtime", end="")

"""elif file_type == "pdf":
        newFile = textract.process(fileLocation, method = "pdfminer")
        file_in = file_in(newFile, 'r')
    elif file_type == "doc":
        newFile = textract.process(fileLocation, method = "antiword")
        file_in = file_in(newFile, 'r')"""
