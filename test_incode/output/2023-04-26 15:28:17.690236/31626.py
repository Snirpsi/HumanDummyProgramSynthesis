#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    numbers_copy = numbers[:]
    
    while numbers:
        number = numbers.pop()
        numbers_copy.remove(number)
        
    print(numbers_copy)
    
