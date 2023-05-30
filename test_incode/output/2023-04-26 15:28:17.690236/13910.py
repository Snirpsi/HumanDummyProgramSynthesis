#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        words.append(line.strip())
    
    # Write words to stdout
    for word in words:
        print(word, end=' ')
        
