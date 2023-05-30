#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port or multiplyes a list of words. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Get the words from the command line
    words = sys.argv[2:]
    
    # Get the words to multiply and store in a list
    words = list(words)
    
    # Iterate through the words and multiply them
    multiplied = []
    for word in words:
        multiplied.append(word*