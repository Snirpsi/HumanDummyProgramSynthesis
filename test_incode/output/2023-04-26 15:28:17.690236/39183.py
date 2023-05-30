#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or adds a list of words. """    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    # Iterate over port
    for port in range(port):
        
        # Iterate over words
        for word in words:
            print(word)
            
