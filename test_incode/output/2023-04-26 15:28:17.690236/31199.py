#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 numbers.py')
        print('Prints the numbers from 1 to 10')
    else:
        number = sys.argv[1]
        
        for i in range(1, 11):
            print('{}: {}'.format(i, number))
            
