#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
        
        numbers_sum = 0
        
        for number in numbers:
            numbers_sum += int(number)
        
        print(numbers_sum)
    else:
        print("Usage: python sum_list.py <numbers>")
        
