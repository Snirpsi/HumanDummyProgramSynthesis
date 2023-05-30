#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words or calculates fruits. """    
    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
        
    # Calculate fruits
    fruits = []
    
    # Calculate fruits
    for word in words:
        fruits.append(word)
        
    # Print fruits
    print('\n'.join(fruits))
    
