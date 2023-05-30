#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or opens a list of words. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            print(number)
        else:
            word = input("Enter a word: ")
            print(word)
