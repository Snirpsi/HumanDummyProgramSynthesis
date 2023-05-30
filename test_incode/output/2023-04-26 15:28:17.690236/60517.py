#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or prints words. """    
    import sys
    
    numbers = sys.argv[1:]
    
    if len(numbers) == 0:
        print('Usage: python remove_numbers.py [numbers]')
        exit()
    
    for number in numbers:
        if number.isdigit():
            print(number)
        else:
            print(number.upper())
    
