#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while(True):
        
        numbers_converted = []
        
        for number in numbers:
            
            numbers_converted.append(number*2)
            
        numbers = numbers_converted
        
        print("Converted numbers: ", numbers)
        
        time.sleep(1)
        
