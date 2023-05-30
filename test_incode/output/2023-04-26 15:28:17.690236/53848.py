#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and opens user input. """    
    
    import sys
    
    number = int(sys.argv[1])
    
    if number > 0 and number < 10:
        print("The number is", number)
    else:
        print("The number is", number, "