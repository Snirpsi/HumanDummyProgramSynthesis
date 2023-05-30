#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or prints user input. """    
    while True:
        number = int(input("Enter a number: "))
        if number < 1:
            print("Invalid input")
        elif number > 100:
            print("Invalid input")
        else:
            print(number)
