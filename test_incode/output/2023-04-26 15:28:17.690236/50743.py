#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            number = str(number)
            
            print(number)
        else:
            print("Error: number must be positive.")
    else:
        print("Usage: python3 number_to_