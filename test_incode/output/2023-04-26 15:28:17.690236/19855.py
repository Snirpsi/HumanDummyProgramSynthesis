#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers. """    
    while True:
        num = input("Enter a number: ")
        try:
            num = int(num)
        except ValueError:
            print("Invalid number")
        else:
            print(num)
