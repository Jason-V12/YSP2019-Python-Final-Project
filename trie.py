"""Implements a trie node. Loads dictionary into memory via trie data structure,
navigates through trie to check spelling, uses trie to suggest similar words.
Writes to output file."""

from time import time


# Struct-like class containing empty string array of children and boolean representing if word
class Node(object):
    def __init__(self):
        self.children = [None] * 41
        self.is_word = False


# Class implementing complete functionality of a trie
class Trie(object):
    def __init__(self, dict_in_use=None):
        # instance variables
        self.parent_node = Node()
        self.traversal_node = self.parent_node
        self.dict_in_use = dict_in_use
        self.word_count = 0
        self.INDEX = 0

    # @param {}
    # @return {boolean} True if successful, else {boolean} False
    # Checks to make sure dictionary is passed in
    def check_dict(self):
        if self.dict_in_use is None:
            return False
        else:
            return True

    # @param {}
    # @return {boolean} True if successful
    # Loads dictionary into Trie data structure
    def add_words(self):
        start_time = time()
        self.traversal_node = self.parent_node
        for cursor in range(0, len(self.dict_in_use)):
            if self.dict_in_use[cursor] == "\'":
                self.INDEX = 26
            elif self.dict_in_use[cursor] == "&":
                self.INDEX = 27
            elif self.dict_in_use[cursor] == "-":
                self.INDEX = 28
            elif self.dict_in_use[cursor] == ".":
                self.INDEX = 29
            elif self.dict_in_use[cursor] == "/":
                self.INDEX = 30
            elif self.dict_in_use[cursor].isalpha():
                self.INDEX = ord(self.dict_in_use[cursor].lower()) - 97
            elif self.dict_in_use[cursor].isnumeric():
                self.INDEX = ord(self.dict_in_use[cursor]) - 17
            else:
                pass
            if self.dict_in_use[cursor] == "\n":
                self.traversal_node.is_word = True
                self.traversal_node = self.parent_node  # Point traversal node back to head node
                self.word_count = self.word_count + 1
            elif self.traversal_node.children[self.INDEX] is None:
                self.traversal_node.children[self.INDEX] = Node()
                self.traversal_node = self.traversal_node.children[self.INDEX]
            else:
                self.traversal_node = self.traversal_node.children[self.INDEX]
        print("Dictionary load time in seconds: " + str(time() - start_time))
        print(self.word_count)
        return True

    # @param {string} word
    # @return {boolean} input_file if successful, else {boolean} False
    # Reads in file from file location specified by user, converts file to .txt if applicable
    def check_word(self, word):
        word = str(word)
        self.traversal_node = self.parent_node
        lower_word = [word[i].lower() for i in range(0, len(word))]
        for letter in range(0, len(lower_word)):
            if lower_word[letter] == "\'":
                if self.traversal_node.children[26] is not None:
                    self.traversal_node = self.traversal_node.children[26]
                else:
                    return False
            elif lower_word[letter] == "&":
                if self.traversal_node.children[27] is not None:
                    self.traversal_node = self.traversal_node.children[27]
                else:
                    return False
            elif lower_word[letter] == "-":
                if self.traversal_node.children[28] is not None:
                    self.traversal_node = self.traversal_node.children[28]
                else:
                    return False
            elif lower_word[letter] == ".":
                if self.traversal_node.children[29] is not None:
                    self.traversal_node = self.traversal_node.children[29]
                else:
                    return False
            elif lower_word[letter] == "/":
                if self.traversal_node.children[30] is not None:
                    self.traversal_node = self.traversal_node.children[30]
                else:
                    return False
            elif lower_word[letter].isalpha():
                try:
                    if self.traversal_node.children[ord(lower_word[letter]) - 97] is not None:
                        self.traversal_node = self.traversal_node.children[ord(lower_word[letter]) - 97]
                    else:
                        return False
                except IndexError:
                    return False
            elif lower_word[letter].isnumeric():
                if self.traversal_node.children[ord(lower_word[letter]) - 17] is not None:
                    self.traversal_node = self.traversal_node.children[ord(lower_word[letter]) - 17]
                else:
                    return False
            else:
                return False
            if letter == len(lower_word) - 1:
                if self.traversal_node.is_word is True:
                    return True
                else:
                    return False

    # @param {string} word
    # @return {string} suggestion if found, else {boolean} False
    # Suggests a word similar to a read-in word, if possible
    def suggestions(self, word):
        self.traversal_node = self.parent_node
        flag = False
        suggestion = ""
        for letter in range(0, len(word)):
            if word[letter] == "\'":
                if self.traversal_node.children[26] is not None:
                    suggestion = suggestion + word[letter]
                    self.traversal_node = self.traversal_node.children[26]
                else:
                    flag = True
            elif word[letter] == "&":
                if self.traversal_node.children[27] is not None:
                    suggestion = suggestion + word[letter]
                    self.traversal_node = self.traversal_node.children[27]
                else:
                    flag = True
            elif word[letter] == "-":
                if self.traversal_node.children[28] is not None:
                    suggestion = suggestion + word[letter]
                    self.traversal_node = self.traversal_node.children[28]
                else:
                    flag = True
            elif word[letter] == ".":
                if self.traversal_node.children[29] is not None:
                    suggestion = suggestion + word[letter]
                    self.traversal_node = self.traversal_node.children[29]
                else:
                    flag = True
            elif word[letter] == "/":
                if self.traversal_node.children[30] is not None:
                    suggestion = suggestion + word[letter]
                    self.traversal_node = self.traversal_node.children[30]
                else:
                    flag = True
            elif word[letter].isalpha():
                try:
                    if self.traversal_node.children[ord(word[letter]) - 97] is not None:
                        suggestion = suggestion + word[letter]
                        self.traversal_node = self.traversal_node.children[ord(word[letter]) - 97]
                    else:
                        flag = True
                except IndexError:
                    return False
            elif word[letter].isnumeric():
                if self.traversal_node.children[ord(word[letter]) - 17] is not None:
                    suggestion = suggestion + word[letter]
                    self.traversal_node = self.traversal_node.children[ord(word[letter]) - 17]
                else:
                    flag = True
            if flag:
                break
        for j in range(0, 15):
            counter = 0
            for i in range(0, 25):
                if self.traversal_node.children[i] is not None:
                    suggestion = suggestion + chr(97 + i)
                    self.traversal_node = self.traversal_node.children[i]
                    counter = counter + 1
                    if self.traversal_node.is_word:
                        return suggestion
