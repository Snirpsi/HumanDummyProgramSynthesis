#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python multiply.py <number>")
        exit()
    
    number = int(sys.argv[1])
    
    product = 1
    
    for i in range(1, number + 1):
        product *= i
    
    print(product)
    
