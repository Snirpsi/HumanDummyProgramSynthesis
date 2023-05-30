#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or removes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print(number)
        else:
            print("Invalid input")
    else:
        print("Usage: python 