#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers or prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0 and number <= 10:
            print(str(number))
        else:
            print("Invalid number")
    else:
        print("Usage: python number