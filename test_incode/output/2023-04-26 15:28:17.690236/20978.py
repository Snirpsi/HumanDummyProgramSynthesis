#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for word in enumerate(' '.join(sys.argv[2:])):
        words.append(word)
        
    print(words)
    
