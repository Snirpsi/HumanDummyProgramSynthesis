#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words. """    
    while True:
        words = list()
        
        # Read words from stdin and store them in words
        for line in sys.stdin:
            words.append(line.strip())
            
        # Calculate list of words and print to stdout
        words.sort()
        
        # Print list of words to stdout
        print('\n'.join(words))
        
        # Sleep for one second
        time.sleep(1)
        
        # Exit the loop
        if words == []:
            break
        
    # 