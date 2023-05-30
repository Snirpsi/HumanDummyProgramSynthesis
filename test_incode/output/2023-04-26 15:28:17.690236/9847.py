#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words or opens user input. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == 'quit':
            break
        
        words.append(word)
    
    return words

<|/ file ext=.py filename=wordlist.py |>