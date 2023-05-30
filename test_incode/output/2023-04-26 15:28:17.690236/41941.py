#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or multiplyes numbers. """    
    while True:
        word = input("Enter a word: ")
        number = input("Enter a number: ")
        number = int(number)
        
        if word == "exit":
            break
        elif word == "multiply":
            number = number * number
        elif word == "add":
            number = number + number
        elif word == "subtract":
            number = number - number
        elif word == "divide":
            number = number / number
        elif word == "multiply