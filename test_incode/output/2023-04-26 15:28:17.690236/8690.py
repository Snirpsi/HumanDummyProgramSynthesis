#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or calculates a list of numbers. """    
    
    # Read command line arguments
    words = []
    numbers = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Ignore empty lines
        if len(line) == 0:
            continue
        
        # Split line into words
        words = line.split(' ')
        
        # Skip empty words
        if len(words) == 0:
            continue
        
        # Calculate numbers
        numbers = [int(x) for x in words]
        
        # Print results
        print(' '.join(map(str, numbers)))
        
    # Print results
    print(' '.join(map(str, numbers)))
    
    # 