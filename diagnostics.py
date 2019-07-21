"""Calculates diagnostic values and outputs to diagnostic file. Details application execution."""

import timeit
class Diagnostics(object):
    def __init__(self):
        #instance variables
        i = 0

    def miss_word_count(self):
        return True
    def dict_word_count(self, fileName):
        file = open(fileName, 'r')
        f = file.read()
        words = f.split()
        count = len(words)
        f.close()
        return count
    def dict_name(self, dicLocation):
        index = repr(dicLocation.rfind('\\')) + 1 
        dicName = dicLocation[index::]
        return dicName
    def file_name(self, fileLocation):
        index = repr(fileLocation.rfind('\\')) + 1 
        fileName = fileLocation[index::]
        return fileName
    def get_time(self):
        return timeit.default_timer()
    def time_calculate(self, start, end):
        return (end - start)
