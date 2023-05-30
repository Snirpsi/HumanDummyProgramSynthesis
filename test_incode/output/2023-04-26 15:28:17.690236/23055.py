#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        number = sys.argv[1]
        
        if number == '*':
            
            print(''.join(map(str, range(1,10))))
            
        elif number == 'remove':
            
            numbers = sys.argv[2:]
            
            print(''.join(map(str, numbers)))
            
        else:
            
            print('Invalid argument')
            
    else:
        
        print('Usage: python -m webserver')
        
    
