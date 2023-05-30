#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    
    numbers = sys.argv[1:]
    
    if len(numbers) == 0:
        print('Usage: python addlist.py <numbers>')
    else:
        numbers = list(map(int, numbers))
        
        numbers = list(map(add, numbers))
        
        print('\n'.join(map(str, numbers)))
