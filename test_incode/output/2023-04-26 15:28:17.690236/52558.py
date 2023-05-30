#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words or stores a list of words. """    
    
    # Get the list of words from the command line
    args = sys.argv[1:]
    words = args.split()
    
    # Convert words to lowercase
    words = [word.lower() for word in words]
    
    # Print the list of words
    for word in words:
        print(word)
        
