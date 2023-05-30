#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of numbers or prints words. """    
    
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    
    words = " ".join(str(i) for i in numbers)
    print(words)
    
