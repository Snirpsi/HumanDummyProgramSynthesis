#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and iterates over numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            print(number)
        except ValueError:
            print("Invalid input. Try again.")
            continue
        else:
            break
    
    
