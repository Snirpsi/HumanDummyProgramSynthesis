#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers. """    
    
    numbers = range(1,10)
    
    while True:
        print(numbers)
        
        numbers = numbers + 1
        
        if numbers == 10:
            break
        
