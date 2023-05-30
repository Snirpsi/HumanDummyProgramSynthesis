#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port and enumerates words. """    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for word in range(port):
        words.append(str(word))
        
    print('\n'.join(words))
    
