#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port or iterates over a list of words. """    
    
    # Get the list of words from the command line
    words = sys.argv[1:]
    
    # Iterate over the list of words and print them out
    for word in words:
        print(word)
        
    # Calculate a port or iterate over a list of words
    port = 1
    for word in words:
        print(word, end=' ')
        port += 1
        if port > 65535:
            port = 1
            
    # Print the list of words and the port number
    print('')
    for word in words:
        print(word, end=' ')
    print(port)
    
