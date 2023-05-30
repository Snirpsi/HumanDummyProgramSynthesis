#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers or adds user input. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: python3 add.py [numbers...]')
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number > 0:
            print(number)
        else:
            print('Invalid number')
    
