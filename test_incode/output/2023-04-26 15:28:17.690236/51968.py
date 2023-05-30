#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers. """    
    
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    
    total = 0
    
    for number in numbers:
        total += number
        
    print("The total is", total)
    
