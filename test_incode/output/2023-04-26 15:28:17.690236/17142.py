#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or stores a list of words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(port):
        words.append(i)
        
    words.sort()
    
    print('\n'.join(words))
    
