#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or opens fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = int(sys.argv[1])
        
        if number > 0:
            
            print('The number is', number, 'multiplied')
            
        else:
            
            print('The number is', number, 'opened')
            
    else:
        
        print('No number given')
        
        
