#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        sys.stdout.write(sys.argv[1])
    else:
        sys.stdout.write('')
    
    sys.stdout.flush()
    
    