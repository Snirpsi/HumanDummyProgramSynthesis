#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or multiplyes words. """    
    
    words = []
    
    for word in sys.argv[1:]:
        words.append(word)
    
    words.sort()
    
    for word in words:
        print(word