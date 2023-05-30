#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and converts a list of words. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words = list(set(words))
    
    for word in words:
        print('