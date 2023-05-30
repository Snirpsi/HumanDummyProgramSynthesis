#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        numbers = sys.argv[1:]
        
        for number in numbers:
            
            print(number)
            
    else:
        
        print('Usage: python remove_numbers.py <numbers>')
        
