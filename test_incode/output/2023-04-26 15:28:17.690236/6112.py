#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or converts numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Invalid input. Try again.")
        else:
            print(number)
