#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input and returns words. """    
    while True:
        word = input("Enter a word: ")
        if word == '':
            break
        else:
            print(word)
            
