#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words and adds a list of words. """    
    while True:
        word = input("Enter a word: ")
        words = word.split()
        
        multiplier = 1
        for word in words:
            multiplier = multiplier * int(word)
        
        print(multiplier)
        
        if word == "quit":
            break
    
