#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input or iterates over numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == 'q':
            break
        else:
            print(number)
    
