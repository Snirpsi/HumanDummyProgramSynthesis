#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or iterates over user input. """    
    while True:
        number = input("Enter a number: ")
        if number == 'q':
            break
        else:
            print(number)
