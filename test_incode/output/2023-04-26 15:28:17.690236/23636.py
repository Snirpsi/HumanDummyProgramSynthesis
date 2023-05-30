#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and prints all ports. """    
    
    import sys
    
    words = set()
    
    for arg in sys.argv[1:]:
        words = words.union(set(arg.split(',')))
    
    words = sorted(list(words))
    
    for word in words:
        print(word)
    
    for port in range(1024, 65535):
        print('