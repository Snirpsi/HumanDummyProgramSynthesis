#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or prints a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if number > 0:
            
            print('The number you entered is ' + str(number))
            
        else:
            
            print('The number you entered is 0')
            
    else:
        
        print('Usage: python add