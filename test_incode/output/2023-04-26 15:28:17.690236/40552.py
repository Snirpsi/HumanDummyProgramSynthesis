#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            number = number * 2
            
            print("The number is", number)
        else:
            print("The number cannot be negative.")
    else:
        print("Usage: python server.py <number>")
    
