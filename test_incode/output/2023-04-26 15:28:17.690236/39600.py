#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or enumerates numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Invalid number")
        else:
            print(number)
