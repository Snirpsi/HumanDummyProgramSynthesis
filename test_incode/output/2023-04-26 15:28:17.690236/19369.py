#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <input>" % sys.argv[0])
        sys.exit()
    
    number = int(sys.argv[1])
    
    if number < 0:
        print("Negative numbers not allowed")
        sys.exit()
    
    number = str(number)
    
    if number == '':
        print("Empty numbers not allowed")
        sys.exit()
    
    number = number.replace('.', '')
    number = number.replace('-', '')
    
    number = float(number)
    
    if number < 0:
        print("Negative numbers cannot be converted to floats")
        sys.exit()
    
    print("The number %s is converted to the number %s" % (number, number))
    
