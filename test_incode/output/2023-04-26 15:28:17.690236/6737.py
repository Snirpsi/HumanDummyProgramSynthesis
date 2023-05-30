#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers or iterates over user input. """    
    
    # iterate over numbers
    for x in numbers:
        print(x)
        
    # iterate over user input
    while True:
        x = input("Enter a number: ")
        try:
            x = int(x)
        except ValueError:
            print("Invalid number")
        else:
            print(x)
            
