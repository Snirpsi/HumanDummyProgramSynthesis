#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers or calculates user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = sys.argv[1]
        
        if number == '1':
            print('1')
        elif number == '2':
            print('2')
        elif number == '3':
            print('3')
        elif number == '4':
            print('4')
        elif number == '5':
            print('5')
        elif number == '6':
            print('6')
        elif number == '7':
            print('7')
        elif number == '8':
            print('8')
        elif number == '9':
            print('9')
        elif number == '0':
            print('0')
        else:
            print('Wrong number')
    else:
        print('Usage: python calculator.py number')
    
