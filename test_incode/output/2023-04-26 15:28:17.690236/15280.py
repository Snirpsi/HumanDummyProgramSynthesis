#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        
        numbers_converted = []
        
        for number in numbers:
            
            numbers_converted.append(str(number))
            
        print('Numbers converted:', numbers_converted)
        
        numbers_converted = numbers_converted[::-1]
        
        print('Numbers converted:', numbers_converted)
        
        numbers_converted = numbers_converted.