#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words or returns a list of words. """    
    words = word_list()
    
    if words:
        print(words)
    else:
        print(word_list())
    
