#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers. """    
    while True:
        num = input("Enter a number: ")
        try:
            num = float(num)
        except ValueError:
            print("That's not a number!")
        else:
            print(num)
            
