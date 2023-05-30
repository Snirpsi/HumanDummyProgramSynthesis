#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or returns words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            number = str(number)
            
            print(number)
        else:
            print(sys.argv[1])
    else:
        print(sys.argv[1])
    
