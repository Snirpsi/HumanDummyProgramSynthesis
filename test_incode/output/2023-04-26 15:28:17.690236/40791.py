#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or prints numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print(number)
        else:
            print("No numbers given")
    else:
        print("No arguments given")
    
