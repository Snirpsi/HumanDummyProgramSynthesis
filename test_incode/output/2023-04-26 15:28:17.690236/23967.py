#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words or stores a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['apple', 'banana', 'orange', 'pear']
    
    words.sort()
    
    for word in words:
        print(word)
    
