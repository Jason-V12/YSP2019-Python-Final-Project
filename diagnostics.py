"""Calculates diagnostic values and outputs to diagnostic file. Details application execution."""

import time
class Diagnostics(object):
    def __init__(self):
            
    def dict_word_count(self, fileName):
        file = open(fileName, 'r')
        f = file.read()
        words = f.split()
        count = len(words)
        f.close()
        writeFile = open("log.txt", "w")
        writeFile.write("There are " + str(count) + " in the dictionary")
        return count
    def dict_name(self, dicLocation):
        index = repr(dicLocation.rfind('\\')) + 1 
        dicName = dicLocation[index::]
        writeFile = open("log.txt", "w")
        writeFile.write("There name of the dictionary is " + dicName)
        return dicName
    def file_name(self, fileLocation):
        index = repr(fileLocation.rfind('\\')) + 1 
        fileName = fileLocation[index::]
        writeFile = open("log.txt", "w")
        writeFile.write("There name of the file is " + dicName)
        return fileName
    def get_time(self):
        return time()
    def time_calculate(self, start, end):
        return (end - start)
