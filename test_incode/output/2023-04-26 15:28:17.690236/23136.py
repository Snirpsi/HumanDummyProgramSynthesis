#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers and enumerates user input. """    
    while True:
        number = input("Enter a number: ")
        if number == 'q':
            break
        else:
            print(number)
            
