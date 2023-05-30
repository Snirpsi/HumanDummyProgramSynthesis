#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number > 10:
            print("You entered a number greater than 10")
        else:
            print(number)
