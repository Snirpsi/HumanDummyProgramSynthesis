#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number < 1:
            print("Invalid input.")
        elif number > 100:
            print("Invalid input.")
        else:
            print(number)
