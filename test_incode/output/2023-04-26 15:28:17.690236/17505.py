#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or adds words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        elif word == 'add':
            word = 'hello'
        elif word == 'remove':
            word = 'world'
        else:
            print("Invalid command")
