# YSP2019-Python-Final-Project
Repository for the SpellChecker final project in YSP Python 2019:

  SpellChecker is a program that aids in checking a text file for spelling errors as efficiently as possible, and recommends similar words to those misspelled. It facilitates multiple languages and unicode characters, which can be chosen by the user. It allows users to upload certain file types for spell checking from their computer. After running, the program will produce a text file containing each misspelled word on a line, followed by suggestions for each word. 

# Usage:
- Note: Program is compatible with the Windows OS
- Download all files as a zip (YSP2019-Python-Final-Project-master.zip)
- Unzip the file, open the directory (SP2019-Python-Final-Project-master)
- Double-click the run.bat file
- If prompted, extract all files to a seperate file location, enter the extracted directory
- If Windows prevents the execution of run.bat, select "More Info" in the popup that appears, then "Run Anyway"
- In the SpellChecker Upload Screen, select a language by clicking a language button
- Then, click the browse button, and locate a .txt file to spell check.
- Once selected, click exit.
- After running, the program will output misspelled words and suggestions to a file named "MisspelledWords.txt"

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
