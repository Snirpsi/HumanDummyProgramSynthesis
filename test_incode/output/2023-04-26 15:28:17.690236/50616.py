#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or prints a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <number|list>' % sys.argv[0])
        sys.exit()
    
    number = sys.argv[1]
    
    if number.isdigit():
        print(int(number))
    elif number.isdigit() or number.isalpha():
        print(list(int(number)))
    else:
        print('Usage: %s <number|list>' % sys.argv[0])
        sys.exit()
