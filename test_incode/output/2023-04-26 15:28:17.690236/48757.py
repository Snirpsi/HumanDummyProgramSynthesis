#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words and iterates over user input. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        else:
            print(word)
            
