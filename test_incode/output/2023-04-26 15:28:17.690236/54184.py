#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input or multiplyes words. """    
    
    word = input("Enter a word: ")
    
    if word == "quit":
        print("Goodbye!")
        exit()
    
    multiplied = word*