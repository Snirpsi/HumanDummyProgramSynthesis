#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            print(number)
        except ValueError as e:
            print("Invalid input. Try again.")
        except 