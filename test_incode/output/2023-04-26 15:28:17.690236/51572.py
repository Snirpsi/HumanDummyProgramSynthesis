#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        
        numbers.append(int(input("Enter a number: ")))
        
        if numbers[-1] == 