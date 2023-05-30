#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and opens user input. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    word