#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Try again.")
        else:
            print(number)
            
