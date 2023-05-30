#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if line == '':
            continue
        
        # Split line into words
        words = line.split(' ')
        
        # Print words to stdout
        for word in words:
            print(word)
        
    # Print final list of words
    print(words)
    
    # Close stdin
    sys.stdin.close()
    
    # Close stdout
    sys.stdout.close()
    
    # Close stderr
    sys.stderr.close()
    
    # Exit with status code 0
    sys.exit(0)

<|/ file source=github |>