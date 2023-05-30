#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and opens user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if number > 0:
            
            print('Removed ' + str(number) + ' numbers from input.')
            
        else:
            
            print('No numbers left from input.')
            
    else:
        
        print('Usage: python remove-numbers-from-input.py <number>')
        
