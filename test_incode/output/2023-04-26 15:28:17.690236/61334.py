#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers or converts numbers. """    
    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Please enter a valid number")
        else:
            print(number)
            
