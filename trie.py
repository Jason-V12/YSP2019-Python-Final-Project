"""Implements a trie node. Loads dictionary into memory via trie data structure,
navigates through trie to check spelling, uses trie to suggest similar words.
Writes to output file."""

from dataclasses import dataclass
from time import time

# Struct-like class containing empty string array of children and boolean representing if word
@dataclass
class Node:
    children = [None] * 41
    is_word = False


class Trie(object):
    def __init__(self, dict_in_use=None):
        # instance variables
        self.head_node = Node()
        self.dict_in_use = dict_in_use
        self.word_count = 0
        self.INDEX = 0

    def check_dict(self):
        if self.dict_in_use is None:
            return False
        else:
            return True

    def add_words(self):
        start_time = time()
        traversal_node = self.head_node  # copy.copy()
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
            else:
                self.INDEX = ord(self.dict_in_use[cursor]) - 17

            if self.dict_in_use[cursor] == "\n":
                traversal_node.is_word = True
                traversal_node = self.head_node  # copy.copy()
                self.word_count = self.word_count + 1
            elif traversal_node.children[self.INDEX] is None:
                traversal_node.children[self.INDEX] = Node()
                traversal_node = traversal_node.children[self.INDEX]
            else:
                traversal_node = traversal_node.children[self.INDEX]
        print("Dictionary load time in seconds: " + str(time() - start_time))
        return True

    def check_word(self, word):
        word = str(word)
        traversal_node = self.head_node  # copy.copy()
        lower_word = [word[i].lower() for i in range(0, len(word))]
        for letter in range(0, len(lower_word)):
            if lower_word[letter] == "\'":
                if traversal_node.children[26] is not None:
                    traversal_node = traversal_node.children[26]
                else:
                    return False
            elif lower_word[letter] == "&":
                if traversal_node.children[27] is not None:
                    traversal_node = traversal_node.children[27]
                else:
                    return False
            elif lower_word[letter] == "-":
                if traversal_node.children[28] is not None:
                    traversal_node = traversal_node.children[28]
                else:
                    return False
            elif lower_word[letter] == ".":
                if traversal_node.children[29] is not None:
                    traversal_node = traversal_node.children[29]
                else:
                    return False
            elif lower_word[letter] == "/":
                if traversal_node.children[30] is not None:
                    traversal_node = traversal_node.children[30]
                else:
                    return False
            elif lower_word[letter].isalpha():
                if traversal_node.children[ord(lower_word[letter]) - 97] is not None:
                    traversal_node = traversal_node.children[ord(lower_word[letter]) - 97]
                else:
                    return False
            else:
                if traversal_node.children[ord(lower_word[letter]) - 17] is not None:
                    traversal_node = traversal_node.children[ord(lower_word[letter]) - 17]
                else:
                    return False
            if letter == len(lower_word) - 1:
                if traversal_node.is_word:
                    return True
                else:
                    return False

