#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers and returns user input. """    
    
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    
    for n in numbers:
        print("The number ", n, " is a prime number.")
        
