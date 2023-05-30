#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers or removes user input. """    
    while True:
        number = int(input("Enter a number: "))
        if number == -1:
            break
        else:
            print(number)
    
