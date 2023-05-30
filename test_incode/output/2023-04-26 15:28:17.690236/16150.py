#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and adds words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    while True:
        words.append(input('> '))
    
    for word in words:
        print(word)
    
