#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number > 0:
            print(number)
        else:
            print('Invalid input')
            
