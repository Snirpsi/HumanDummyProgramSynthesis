#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or prints fruits. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        else:
            print(word)
