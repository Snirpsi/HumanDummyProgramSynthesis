#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or calculates a list of words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        else:
            print(word*2)
