#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers. """    
    
    while True:
        numbers = input("Enter a number: ")
        numbers = list(map(int, numbers.split()))
        
        if len(numbers) == 0:
            break
        
        numbers.append(