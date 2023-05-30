#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = sys.argv[1]
        
        try:
            number = int(number)
        except ValueError:
            print("Invalid number")
            sys.exit(1)
            
        if number > 100 or number < 0:
            print("Invalid number")
            sys.exit(1)
            
        print(number)
    else:
        print("Usage:")
        print("  python3 number_to_