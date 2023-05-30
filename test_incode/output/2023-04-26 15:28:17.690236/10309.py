#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and returns a list of words. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    print(" ".join(words))
    
