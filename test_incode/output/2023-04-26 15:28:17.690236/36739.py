#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        print("The next number is", numbers.pop(0))
        
        if numbers:
            print("The next number is", numbers.pop(0))
            
        else:
            break
        
    print("The end!")
    
