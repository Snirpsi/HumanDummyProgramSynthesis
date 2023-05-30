#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers and iterates over user input. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Invalid number")
        else:
            print(number)
            
