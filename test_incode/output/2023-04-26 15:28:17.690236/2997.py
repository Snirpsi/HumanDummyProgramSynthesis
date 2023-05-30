#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words or opens a list of numbers. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        else:
            print(word)
    
    
<|/ file source=github filename=