#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers or calculates fruits. """    
    
    numbers = range(1,10)
    fruits = []
    
    for number in numbers:
        fruits.append(number)
        
    print(numbers)
    print(fruits)
    
