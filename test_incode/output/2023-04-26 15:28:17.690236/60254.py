#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    words = []
    
    # Read all words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Skip empty lines
        if not line.isspace():
            words.append(line)
            
    # Print the list of words
    print(words)
    
    # 