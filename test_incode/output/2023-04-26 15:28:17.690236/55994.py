#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    i = 0
    while True:
        print(numbers[i])
        i += 1
        if i == len(numbers):
            break
        
