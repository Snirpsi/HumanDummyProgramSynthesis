#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers or converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python %s number" % sys.argv[0])
        exit()
    
    number = sys.argv[1]
    
    if number.isdigit():
        number = int(number)
    
    result = number * number
    
    print("The result is:", result)
    
