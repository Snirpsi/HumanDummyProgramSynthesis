#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or removes numbers. """    
    
    import sys
    
    number = int(sys.argv[1])
    
    if number > 0:
        numbers = range(number)
        
        for number in numbers:
            print(number)
    else:
        print("No number given.")
    
