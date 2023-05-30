#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [fruits]" % sys.argv[0])
        sys.exit()
    
    fruits = sys.argv[1:]
    
    if len(fruits) == 0:
        print("Usage: %s [fruits]" % sys.argv[0])
        sys.exit()
    
    fruits = fruits.split(',')
    
    fruits = [int(f) for f in fruits]
    
    fruits_sum = 0
    
    for f in fruits:
        fruits_sum += f
    
    print("The sum of the numbers: ", fruits_sum)
    
