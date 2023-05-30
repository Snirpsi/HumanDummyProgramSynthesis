#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input. """    
    while True:
        multiplier = int(input("Enter a number: "))
        multiplier = multiplier * 2
        print("The product of {} and {} is {}".format(multiplier, multiplier, multiplier * 2))
        
