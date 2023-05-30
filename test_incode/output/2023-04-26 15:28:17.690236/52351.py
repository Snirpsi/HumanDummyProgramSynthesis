#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words or returns fruits. """    
    
    # Get the words from the file
    with open('words.txt', 'r') as f:
        words = f.read().split()
        
    # Iterate over words and print them out
    for word in words:
        print(word)
        
    # Get the fruits from the file
    with open('fruits.txt', 'r') as f:
        fruits = f.read().split()
        
    # Iterate over fruits and print them out
    for fruit in fruits:
        print(fruit)
        
