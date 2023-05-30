#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        
        try:
            number = int(number)
        except ValueError:
            print('Error')
            continue
        
        if number < 0:
            print('Error')
            continue
        
        if number > 0:
            print('Removed', number, 'numbers')
        else:
            print('Error')
            continue
    
    print('Done')
    
