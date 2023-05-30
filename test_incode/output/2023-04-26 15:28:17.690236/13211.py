#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or iterates over numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = sys.argv[1]
        
        if number.isdigit():
            number = int(number)
            
            if number > 0:
                sys.stdout.write(str(number))
            else:
                sys.stdout.write('\n')
        else:
            for number in sys.argv[1:]:
                sys.stdout.write(str(number))
                sys.stdout.write('\n')
    else:
        number = int(input('Enter a number: '))
        
        if number > 0:
            sys.stdout.write(str(number))
        else:
            sys.stdout.write('\n')
    
