#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        word = str(input("Enter a word: "))
        
        if word == "quit":
            break
        
        multiplier = 1
        for char in word:
            multiplier = multiplier * char
            
        print(multiplier)
        
