#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words or multiplyes a list of words. """    
    
    words = []
    
    # Open the file
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
        
    # Multiply each word in the file
    for word in words:
        print(word*2)
        
    # Close the file
    file.close()
    
