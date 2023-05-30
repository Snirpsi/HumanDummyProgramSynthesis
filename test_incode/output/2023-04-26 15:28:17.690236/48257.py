#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = ""
    
    words = []
    with open(filename) as f:
        for line in f:
            words.append(line.strip())
    
    print(" ".join(words))
    
