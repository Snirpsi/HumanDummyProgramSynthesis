#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and iterates over all ports. """    
    
    words = []
    
    while True:
        words.append(input("Enter a word: "))
        
        if len(words) == 