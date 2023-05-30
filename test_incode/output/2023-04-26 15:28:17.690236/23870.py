#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Try again.")
    
    print("The number you entered is", number)
    
