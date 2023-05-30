#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers. """    
    while True:
        try:
            n = int(input("Enter a number: "))
        except ValueError:
            print("Invalid number. Try again.")
        else:
            print("The number is", n)
            
