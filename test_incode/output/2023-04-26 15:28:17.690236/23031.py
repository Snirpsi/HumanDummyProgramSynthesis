#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers or opens a list of numbers. """    
    
    numbers = range(10)
    
    for number in numbers:
        print(number)
        
        if number == 10:
            break
        
