#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and calculates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(0, 10):
        words.append(str(i))
    
    words.sort()
    
    word