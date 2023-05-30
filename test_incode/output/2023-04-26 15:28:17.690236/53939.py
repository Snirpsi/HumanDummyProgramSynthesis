#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers or converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python list.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number > 0:
            print(number)
        else:
            print("0")
    
