#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python multiply.py <num1> <num2>')
    else:
        num1 = sys.argv[1]
        num2 = sys.argv[2]
        
        print(num1 * num2)
    
