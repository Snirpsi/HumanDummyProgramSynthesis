#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or converts numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("That was not a valid number. Try again.")
        else:
            print(number)
            
