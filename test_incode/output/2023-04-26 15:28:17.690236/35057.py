#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        
        numbers.append(numbers[-1] + numbers[-2])
        
        if numbers[-1] == numbers[-2]:
            
            numbers.pop()
            
        else:
            
            break
        
    print(numbers)
    
