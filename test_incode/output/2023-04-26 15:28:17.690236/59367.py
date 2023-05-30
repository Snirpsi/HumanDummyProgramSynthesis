#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers or multiplyes numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            break
        else:
            print(number * 2)
