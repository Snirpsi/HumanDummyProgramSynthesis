#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or stores fruits. """    
    while True:
        word = input("Enter a word: ")
        fruits = input("Enter a fruit: ")
        if fruits == "quit":
            break
        else:
            print(word*fruits)
