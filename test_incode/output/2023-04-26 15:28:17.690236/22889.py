#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words and calculates a port. """    
    words = word_list()
    port = 1
    
    for word in words:
        port *= len(word)
    
    print(port)
    
