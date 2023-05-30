#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or returns numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'word':
            print('word')
        elif word == 'number':
            print('number')
        else:
            print('unknown word')
    else:
        print('usage: python word