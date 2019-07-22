"""Calculates diagnostic values and outputs to diagnostic file. Details application execution."""

from time import time


class Diagnostics(object):
    def __init__(self, code):
        self.code = code

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
        dicName = dicLocation
        writeFile = open("log.txt", "w")
        writeFile.write("The name of the dictionary is " + dicName)
        return dicName
    def file_name(self, fileLocation):
        fileName = fileLocation
        writeFile = open("log.txt", "w")
        writeFile.write("The name of the file is " + fileName)
        return fileName
    def get_time(self):
        return time()
    def time_calculate(self, start, end):
        return (end - start)
    def return_code(self):
        return self.code
