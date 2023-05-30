#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or calculates a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Read user input from stdin
        
        number = int(sys.argv[1])
        
    else:
        
        # Calculate list of numbers
        
        numbers = [1,2,3,4,5,6,7,8,9]
        
    
    # Print the results
    
    for number in numbers:
        
        print(number)
        
    
    # 