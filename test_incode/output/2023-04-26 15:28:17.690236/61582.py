#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(1, port+1):
        words.append(i)
    
    words.sort()
    
    print('\n'.join(words))
    
