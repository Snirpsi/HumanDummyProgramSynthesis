#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers and opens numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers_cleaned = []
    
    for number in numbers:
        
        try:
            number = int(number)
        except ValueError:
            
            numbers_cleaned.append(number)
            
        else:
            
            numbers_cleaned.append(number)
            
    numbers_cleaned = list(set(numbers_cleaned))
    
    numbers_open = []
    
    for number in numbers_cleaned:
        
        try:
            number = int(number)
        except ValueError:
            
            numbers_open.append(number)
            
        else:
            
            numbers_open.append(number)
            
    numbers_open = list(set(numbers_open))
    
    numbers_open = sorted(numbers_open)
    
    for number in numbers_open:
        
        print(number)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    