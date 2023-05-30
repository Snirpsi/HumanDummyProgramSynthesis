#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words or iterates over a list of words. """    
    words = []
    
    # Open the word list
    with open('words.txt', 'r') as f:
        words = f.readlines()
    
    # Iterate over the words in the word list
    for word in words:
        print(word)
        
    # Close the word list
    f.close()
    
