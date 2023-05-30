#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        number = numbers.pop(0)
        
        if number == 10:
            break
        
        print(number)
        
