#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number < 1:
            print("Invalid number. Try again.")
        elif number > 100:
            print("Invalid number. Try again.")
        else:
            print(number)
