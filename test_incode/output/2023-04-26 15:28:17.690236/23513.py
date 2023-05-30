#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and removes a list of words. """    
    words = []
    
    # Open the file
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    # Remove words from the list
    words = [word for word in words if word not in ['