#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or iterates over a list of numbers. """    
    
    while True:
        number = int(input("Enter a number: "))
        
        if number == 9999:
            break
        
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")
        
