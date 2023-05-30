#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and removes a list of words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    # Read words from a file
    with open('words.txt', 'r') as f:
        words = [word.strip() for word in f.readlines()]
    
    # Remove words from a list
    words = [word for word in words if word not in words]
    
    # Return the port and words
    return port, words
    
    
