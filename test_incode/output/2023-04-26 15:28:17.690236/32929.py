#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or prints a list of numbers. """    
    while True:
        word = input("Enter a word: ")
        if word == 'q':
            break
        number = int(input("Enter a number: "))
        print(word, number)
