#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    numbers = range(1,11)
    
    while True:
        number = input("Enter a number: ")
        if number in numbers:
            print(number)
        else:
            print("That number is not in the list")
            
