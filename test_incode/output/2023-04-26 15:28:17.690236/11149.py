#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and calculates words. """    
    
    words = []
    
    while True:
        words.append(input("Enter a word: "))
        
        if words[-1] == "stop":
            break
        
    print(" ".join(words))
    
