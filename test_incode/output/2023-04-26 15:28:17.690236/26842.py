#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            sys.stdout.write(str(number))
        else:
            sys.stdout.write("0")
    else:
        sys.stdout.write("0")
    
    