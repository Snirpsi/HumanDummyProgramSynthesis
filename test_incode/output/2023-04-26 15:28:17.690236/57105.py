#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port and iterates over a list of numbers. """    
    
    port = 1
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        number = numbers.pop(0)
        
        port *= number
        
        print('Port multiplied by 