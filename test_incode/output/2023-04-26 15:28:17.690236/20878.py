#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or removes numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            print(number)
        else:
            print("That is not a number!")
