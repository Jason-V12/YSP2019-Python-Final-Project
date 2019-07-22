# YSP2019-Python-Final-Project
Repository for the SpellCheck final project in YSP Python 2019:

  SpellCheck is a program that aids in checking a text file for spelling errors as efficiently as possible, and recommends similar words to those misspelled. It facilitates multiple languages and unicode characters, which can be chosen by the user. It allows users to upload certain file types for spell checking from their computer. After running, the program will produce a text file containing each misspelled word on a line, followed by the line number of misspelled words, and up to three suggestions for each word. 
  The user can also type words into the program that will be inserted into the dictionary, which will not be flagged as misspelled by the program (e.g. names, archaic words, etc), just like MS word and google spell checking programs. The program will also skip words that contain numbers, such as addresses and phone numbers, as well as words in all uppercase (also similar to MS word and google spell checking).
# Usage:

# Error codes:
- 0: Successful run 
- 1: Interface failure
- 2: Dictionary selection failure
- 3: Input file load failure

# Imports: 
 - from string import punctuation
 - from dataclasses import dataclass
 - from time import time
 - from tkinter import *
 - from tkinter.filedialog import askopenfilename
 - from tika import parser

# Seperation of Work:
- Jason worked on the trie.py file and coded the trie data structure as well as the main method in the __init__.py file
- Srikar coded the GUI using Tkinter
- Ani worked on the diagnostics.py file and coded all the functions as well as the get_file function in the __init__.py file

# Goals:
- All of our goals were met except for one: converting PDF and DOC to TXT
    - We parse through the PDF, which isn't the same as converting the file, but it is just as effecient
    - We aren't 100% sure it works, but we included it

# Credits:
This application uses Open Source components. You can find the source code of their open source projects along with license information below. We acknowledge and are grateful to these developers for their contributions to open source.

EnglishDictionary.txt: 

Project: english-words https://github.com/dwyl/english-words

Copyright (c) 2018, Infochimps (https://web.archive.org/web/20131118073324/http://www.infochimps.com/datasets/word-list-350000-simple-english-words-excel-readable)

Tkinter: https://pythonspot.com/tk-file-dialogs/


3Parsing through pdf: https://medium.com/@justinboylantoomey/fast-text-extraction-with-python-and-tika-41ac34b0fe61
