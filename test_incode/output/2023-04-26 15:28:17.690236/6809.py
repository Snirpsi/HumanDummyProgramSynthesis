#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words. """    
    while True:
        words = []
        
        # Read a line from stdin
        line = sys.stdin.readline()
        
        # Break out of the loop if we get a blank line
        if not line:
            break
        
        # Split the line into words
        words = line.split()
        
        # Print the list of words
        print('\n'.join(words))
        
        # Sleep for one second
        time.sleep(1)
        
    # Print the final 