#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    
    import sys
    
    number = sys.argv[1]
    
    try:
        number = float(number)
    except ValueError:
        print("Error: number must be float.")
        sys.exit()
    
    print(number)
    
