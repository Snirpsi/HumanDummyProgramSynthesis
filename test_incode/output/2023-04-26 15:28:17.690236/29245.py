#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and prints words. """    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(1, port+1):
        words.append(i)
    
    print('\n'.join(words))
    
