#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or multiplyes words. """    
    while True:
        word = input("Enter a word: ")
        if word == '':
            break
        else:
            print(word*2)
