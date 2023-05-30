#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 remove-words-from-file.py')
        sys.exit()
    
    removeWordsFromFile(sys.argv[1])
    
