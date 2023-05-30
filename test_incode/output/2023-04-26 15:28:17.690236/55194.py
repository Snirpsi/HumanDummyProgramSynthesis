#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words or iterates over a port. """    
    import sys
    import time
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        sys.stdout.write('\n')
        sys.stdout.flush()
        
        for word in words:
            sys.stdout.write('*' * len(word))
            sys.stdout.write(word)
            sys.stdout.write('\n')
        
        time.sleep(1)
        
