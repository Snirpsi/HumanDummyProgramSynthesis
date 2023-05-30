#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and iterates over words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    for word in words:
        print(word)
        
