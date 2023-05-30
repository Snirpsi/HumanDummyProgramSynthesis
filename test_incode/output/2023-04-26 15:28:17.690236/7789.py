#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and prints user input. """    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        print(word)
        
