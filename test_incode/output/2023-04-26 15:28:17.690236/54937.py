#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or multiplyes words. """    
    while True:
        number = input("Enter a number: ")
        word = input("Enter a word: ")
        if number == word:
            print("Congratulations! You guessed the number!")
            break
        else:
            print("Sorry! You guessed the wrong number!")
