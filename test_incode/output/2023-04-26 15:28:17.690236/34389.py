#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words. """    
    
    # Create a list with all the words in the file
    words = open('words.txt').read().split()
    
    # Iterate over the words and print them out
    for word in words:
        print(word)
        
    # Close the file
    words.close()
    
