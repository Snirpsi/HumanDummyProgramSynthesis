#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'user':
            
            print('Enter a number:')
            
            number = int(input('Enter a number: '))
            
            print('The product of %d and %d is %d.' % (number, number, number * number))
            
        elif sys.argv[1] == 'number':
            
            print('Enter a number:')
            
            number = int(input('Enter a number: '))
            
            print('The product of %d and %d is %d.' % (number, number, number * number))
            
        else:
            
            print('Usage: python webserver.py [user|number]')
            
    else:
        
        print('Usage: python webserver.py [user|number]')
    
