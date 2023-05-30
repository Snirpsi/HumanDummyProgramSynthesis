#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words. """    
    
    # Open the file that contains the list of words
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Enumerate the words and print them out
    for word in words:
        print(word)
        
