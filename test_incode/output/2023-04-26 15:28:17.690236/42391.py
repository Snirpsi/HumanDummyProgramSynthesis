#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words or stores numbers. """    
    while True:
        words = [input("Enter a word: ")] 
        numbers = [int(i) for i in input("Enter a numbers: ").split()]
        
        