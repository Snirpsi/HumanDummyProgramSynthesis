#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input or removes numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Invalid input")
        else:
            break
    return number
