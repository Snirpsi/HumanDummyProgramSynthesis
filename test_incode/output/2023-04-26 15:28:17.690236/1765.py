#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or multiplyes numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    
    while True:
        try:
            multiplier = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    
    while True:
        try:
            number = number * multiplier
            break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    
    print("The product of {} and {} is {}.".format(number, multiplier, number))
    
