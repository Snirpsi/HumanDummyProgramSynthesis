#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words or enumerates words. """    
    
    # Get the words from the file
    words = open(sys.argv[1]).read().splitlines()
    
    # Print the words
    for word in words:
        print(word)
        
    # Print the enumerated words
    for index, word in enumerate(words):
        print(index, word)
        
    # Close the file
    words.close()
    
