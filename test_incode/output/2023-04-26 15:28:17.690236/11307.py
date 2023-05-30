#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers or returns user input. """    
    while True:
        number = input("Enter a number: ")
        if number == "quit":
            break
        elif number.isdigit():
            number = int(number)
            print(number)
        else:
            print("Please enter a number.")
    
    
