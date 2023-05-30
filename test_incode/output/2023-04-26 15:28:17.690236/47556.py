#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or adds numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        try:
            number = int(number)
        except ValueError:
            print("Invalid number: %s" % number)
            sys.exit()
        
        if number > 0:
            print(number)
        else:
            print("0")
            
