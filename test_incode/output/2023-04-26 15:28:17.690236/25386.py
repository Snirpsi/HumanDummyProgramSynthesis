#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words and returns user input. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == "":
            break
        
        words.append(word)
    
    return words
