#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if number > 0:
            
            print('You entered ' + str(number))
            
        else:
            
            print('You entered a negative number')
            
    else:
        
        print('You did not enter a number')
        
    
