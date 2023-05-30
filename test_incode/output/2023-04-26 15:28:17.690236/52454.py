#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or adds numbers. """    
    while True:
        try:
            num = input("Enter a number: ")
            num = float(num)
            print(num)
            break
        except ValueError:
            print("Invalid input. Try again.")
            continue
