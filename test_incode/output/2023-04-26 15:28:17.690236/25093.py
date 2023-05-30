#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number> [<number> ...]" % sys.argv[0])
        sys.exit()
    
    numbers = []
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
    
    numbers.sort()
    
    for number in numbers:
        print(number)
        
