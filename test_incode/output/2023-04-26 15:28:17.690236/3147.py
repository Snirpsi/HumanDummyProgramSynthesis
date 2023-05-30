#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or opens user input. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        else:
            print(word)
    
