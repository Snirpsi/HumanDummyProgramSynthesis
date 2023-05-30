#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    numbers = [int(i) for i in input().split()]
    
    while True:
        converted = []
        
        for number in numbers:
            converted.append(number * 10)
        
        print(*converted, sep='')
        
        numbers = converted
        
        if numbers == []:
            break
        
