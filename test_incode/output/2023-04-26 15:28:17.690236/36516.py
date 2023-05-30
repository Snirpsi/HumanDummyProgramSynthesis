#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and enumerates user input. """    
    
    numbers = input("Enter numbers: ").split()
    
    for number in numbers:
        print(number)
    
    print("Done.")
    
