#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or stores words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    while True:
        words.append(str(input('Enter a word: ')))
    
    words.sort()
    
    