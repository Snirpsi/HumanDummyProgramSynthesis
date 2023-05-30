#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input and returns numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number < 1:
            print("Invalid input. Try again.")
        else:
            break
    return number
