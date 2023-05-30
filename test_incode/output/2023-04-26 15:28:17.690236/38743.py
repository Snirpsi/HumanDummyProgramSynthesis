#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and returns a port. """    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for word in open('words.txt'):
        words.append(word.rstrip())
    
    words.sort()
    
    for word in words:
        print(word)
        
    