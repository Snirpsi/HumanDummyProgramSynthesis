#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or multiplyes fruits. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words.sort()
    
    multiplied = []
    
    for word in words:
        multiplied.append(word*2)
    
    print(" ".join(multiplied))
    
