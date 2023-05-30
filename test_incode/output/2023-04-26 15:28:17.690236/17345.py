#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and stores words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for _ in range(port):
        words.append(input())
    
    print('\n'.join(words))
    
    
