#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words and multiplyes a list of numbers. """    
    while True:
        word = input("Enter a word: ")
        number = input("Enter a number: ")
        numbers = [int(i) for i in number.split()]
        numbers = [number * i for i in numbers]
        print(" ".join(word