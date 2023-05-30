#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or calculates a list of numbers. """    
    
    words = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3]
    
    while True:
        
        number = input('Enter a number: ')
        
        if number == 'done':
            break
        
        if number in words:
            print(number)
        
        else:
            print(number * number