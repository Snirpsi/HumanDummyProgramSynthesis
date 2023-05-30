#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            number = number - 1
            
            if number < 0:
                number = number + 1
            
            print(number)
            
        else:
            print("Please give a positive number")
            
    else:
        print("Please give a positive number")
    
