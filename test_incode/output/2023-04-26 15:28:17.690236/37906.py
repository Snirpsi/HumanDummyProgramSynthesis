#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = 1
    
    print("The number is", number*number)
    
