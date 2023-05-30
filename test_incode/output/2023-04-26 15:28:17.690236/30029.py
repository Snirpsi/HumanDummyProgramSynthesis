#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <num1> <num2> ..." % sys.argv[0])
        sys.exit()
    
    numbers = []
    for arg in sys.argv[1:]:
        try:
            numbers.append(int(arg))
        except ValueError:
            print("Error: %s is not a valid number." % arg)
            sys.exit()
    
    numbers = numbers * 2
    
    for number in numbers:
        print(number)
    
