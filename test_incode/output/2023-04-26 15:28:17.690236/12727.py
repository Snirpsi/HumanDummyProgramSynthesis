#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or opens a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            print(int(number))
        else:
            print("Please enter only digits.")
