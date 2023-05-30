#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0 and number <= 10:
            print(number)
        else:
            print('Invalid input')
    else:
        print('Usage: python3 number_generator.py <number>')
        
