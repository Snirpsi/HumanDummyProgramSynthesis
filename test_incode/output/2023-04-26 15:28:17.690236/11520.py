#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or returns numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word in ['words', 'numbers']:
            print(word)
        else:
            print(word)
    else:
        print('Usage: python wordlist.py [words]')
        
