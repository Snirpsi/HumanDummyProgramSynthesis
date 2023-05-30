#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python remove_numbers.py <numbers>')
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
    
        if number > 0:
            print(number)
        else:
            print('')
    
