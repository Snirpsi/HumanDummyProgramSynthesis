#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if number > 0 and number < 1000000:
            
            print(number)
            
        else:
            
            print("Number must be between 0 and 1000000.")
            
    else:
        
        print("Usage: python3 number