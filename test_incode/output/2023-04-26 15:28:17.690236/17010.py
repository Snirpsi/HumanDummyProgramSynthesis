#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers. """    
    
    number = int(input("Enter a number: "))
    
    if number > 0 and number <= 10:
        print("The number {} is prime".format(number))
    else:
        print("The number {} is not prime".format(number))
    
