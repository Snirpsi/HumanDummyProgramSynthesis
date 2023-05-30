#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        words.append(line.strip())
        
    # Write words to stdout
    for line in words:
        print(line, end='')
        
    # 