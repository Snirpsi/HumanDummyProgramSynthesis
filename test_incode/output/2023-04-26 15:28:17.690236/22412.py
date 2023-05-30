#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or opens a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            number = str(number)
        else:
            number = str(number)
            
        print("The number is: " + number)
    else:
        print("No number given")
    
