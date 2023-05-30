#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers or stores words. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            print(number)
        else:
            word = input("Enter a word: ")
            print(word)
