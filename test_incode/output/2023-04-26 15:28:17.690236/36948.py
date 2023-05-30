#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Ignore empty lines
        if len(line) == 0:
            continue
        
        # Split line into words
        words = line.split(' ')
        
        # Store words in list
        words.extend(words)
    
    # Write words to stdout
    print(' '.join(words))
    
    # Close stdin
    sys.stdin.close()
    
    # Close stdout
    sys.stdout.close()
    
    # Close stderr
    sys.stderr.close()
    
    # Exit program
    sys.exit(0)
