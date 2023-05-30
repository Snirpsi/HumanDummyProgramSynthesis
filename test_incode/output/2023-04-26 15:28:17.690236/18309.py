#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and iterates over a port. """    
    words = []
    port = 8080
    
    while True:
        words.append(input("Enter a word: "))
        
        if len(words) == port:
            break
        
        print("