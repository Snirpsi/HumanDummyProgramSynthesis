#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and converts user input. """    
    import sys
    port = sys.argv[1]
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words.sort()
    
    word