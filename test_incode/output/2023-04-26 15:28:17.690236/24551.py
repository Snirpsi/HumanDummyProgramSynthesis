#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and prints numbers. """    
    
    words = ["cat", "dog", "bird", "snake", "mouse"]
    
    for index, word in enumerate(words):
        print("{}. {}".format(index, word))
    
