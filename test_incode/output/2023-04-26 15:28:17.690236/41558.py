#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or multiplyes numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            if number > 0:
                print("The number you entered is greater than 0")
            else:
                print("The number you entered is less than 0")
        else:
            print("You did not enter a number")
