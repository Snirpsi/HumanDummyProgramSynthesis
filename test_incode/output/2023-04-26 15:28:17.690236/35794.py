#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers and iterates over numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Invalid input. Try again.")
            continue
        else:
            print(number)
            
