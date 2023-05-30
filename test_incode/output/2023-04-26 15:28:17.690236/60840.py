#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or adds a list of words. """    
    
    words = []
    
    while True:
        
        words.append(input("Enter a word: "))
        
        if words[-1] == 'q':
            break
        
    words.extend(["q", "quit", "exit", "q