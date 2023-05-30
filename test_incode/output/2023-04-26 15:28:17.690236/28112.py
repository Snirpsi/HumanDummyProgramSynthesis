#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s number" % sys.argv[0])
        sys.exit(1)
    
    number = sys.argv[1]
    
    if number < 10:
        print("%d is too small" % number)
        sys.exit(1)
    
    for i in range(number):
        print(i)
        
    print("Done!")

<|/ file ext=.py source=github |>