#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and calculates words. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    words = []
    for port in ports:
        words.extend(calc_words(port))
    
    print('\n'.join(words))
    
    
