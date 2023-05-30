#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or converts a list of numbers. """    
    import sys
    port = int(sys.argv[1])
    
    numbers = []
    for arg in sys.argv[2:]:
        try:
            numbers.append(int(arg))
        except ValueError:
            print("Invalid number: %s" % arg)
            sys.exit(1)
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    numbers_str = ""
    for number in numbers:
        numbers_str += str(number) + " "
    
    print(numbers_str)
    
    
