#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split by whitespace
        words = line.split()
        
        # Print the word
        print(' '.join(words))
        
    # Print the final list
    print(' '.join(words))
    
    # Close the file
    f.close()
    
    # Close the program
    exit(0)
    
# EOF

<|/ file source=github filename=wordlist.py |>