#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or prints numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            print(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        else:
            break
