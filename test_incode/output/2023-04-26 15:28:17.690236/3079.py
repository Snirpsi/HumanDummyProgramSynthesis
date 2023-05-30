#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            number = number - 1
            
            print(str(number))
        else:
            print('Invalid number.')
    else:
        print('Usage: python remove_numbers.py <number>')
        
