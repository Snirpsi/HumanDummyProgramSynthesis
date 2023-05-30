#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and returns user input. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words = ' '.join(words)
    
    print('\n'.join(words))
    
