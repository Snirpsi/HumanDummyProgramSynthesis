#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or calculates a port. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['word1', 'word2', 'word3']
    
    words.sort()
    
    for word in words:
        print(word)
        
    
<|/ file ext=.py filename=