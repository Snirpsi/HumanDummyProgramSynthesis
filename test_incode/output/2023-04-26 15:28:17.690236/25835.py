#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or calculates numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            if number > 0:
                print("The number you entered is", number)
            else:
                print("The number you entered is", number*-1)
        else:
            print("Please input a number!")
