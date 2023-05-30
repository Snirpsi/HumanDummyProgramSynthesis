#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or converts numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        numbers = sys.argv[1:]
        
        for number in numbers:
            
            print(number)
            
    else:
        
        print('Usage: python3 converter.py <numbers>')
        
