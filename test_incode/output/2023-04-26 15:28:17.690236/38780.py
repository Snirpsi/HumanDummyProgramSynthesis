#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words. """    
    
    words = []
    
    for word in sys.argv[1:]:
        words.append(word)
    
    print(words)
    
