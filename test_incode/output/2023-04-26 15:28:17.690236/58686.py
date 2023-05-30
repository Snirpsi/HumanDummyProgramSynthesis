#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port and converts a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    for word in words:
        print(word, end=' ')
        
        if port == 80:
            print(' ', end=' ')
        
        port -= 1
    
