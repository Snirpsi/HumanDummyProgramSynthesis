#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    numbers_multiplied = []
    
    while len(numbers) > 0:
        numbers_multiplied.append(numbers[0]*numbers.pop(0))
        
    print(numbers_multiplied)
    
