#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == 'userinput':
            
            print('Enter a number:')
            
            number = int(input())
            
            print('The product of %d and %d is %d.' % (number, number, number * number))
            
        else:
            
            print('Enter a number:')
            
            number = int(input())
            
            print('The product of %d and %d is %d.' % (number, number, number * number))
            
    else:
        
        print('Enter a number:')
        
        number = int(input())
        
        print('The product of %d and %d is %d.' % (number, number, number * number))
        
    
