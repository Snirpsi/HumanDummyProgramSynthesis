#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers. """    
    import sys
    
    number = int(sys.argv[1])
    
    if number > 10:
        print("Too big")
    elif number < 1:
        print("Too small")
    else:
        print(number)
    
