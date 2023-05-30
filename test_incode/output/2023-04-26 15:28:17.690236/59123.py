#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            number = number - 1
            
            sys.stdout.write(str(number))
            sys.stdout.flush()
        else:
            sys.stdout.write('0')
            sys.stdout.flush()
    else:
        sys.stdout.write('0')
        sys.stdout.flush()
        
