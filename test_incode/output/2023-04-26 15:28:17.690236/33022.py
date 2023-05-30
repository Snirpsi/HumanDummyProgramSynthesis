#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or opens numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'add':
            
            number = int(sys.argv[2])
            
            number = str(number)
            
            print('You entered', number, '