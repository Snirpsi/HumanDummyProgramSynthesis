#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or multiplyes words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        elif word == 'quit\n':
            break
        else:
            print(word)
            print(word*2)
