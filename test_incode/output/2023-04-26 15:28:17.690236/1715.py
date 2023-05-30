#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits or enumerates numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "quit":
            break
        elif number.isdigit():
            print(int(number))
        else:
            print("Invalid number")
