#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or removes a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input("Enter a number: "))
    
    if number > 0:
        print("Number:", number)
    elif number < 0:
        print("Number:", -number)
    else:
        print("Number:", number)
    
