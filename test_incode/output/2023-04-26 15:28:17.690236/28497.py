#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits or converts words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python fruits.py [word]")
        exit(1)
    
    word = sys.argv[1]
    
    fruits = Fruits(word)
    
    for fruit in fruits:
        print(fruit)
    
    
