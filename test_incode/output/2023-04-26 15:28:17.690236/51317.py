#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or prints words. """    
    import sys
    
    if len(sys.argv) > 1:
        
        number = sys.argv[1]
        
        if number.isdigit():
            
            print(number)
            
        else:
            
            print(number.upper())
            
    else:
        
        print("Usage: python3 remove-numbers.py <number>")
        
