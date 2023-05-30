#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or returns a port. """    
    import sys
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = 'hello'
    print(word)
