#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or opens numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Try again.")
    
    if number % 2 == 0:
        print("Even number:", number)
    else:
        print("Odd number:", number)
    
