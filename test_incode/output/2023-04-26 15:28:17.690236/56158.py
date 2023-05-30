#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and calculates a list of words. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    words = []
    for port in ports:
        words.append(str(port))
    
    print('\n'.join(words))
    
