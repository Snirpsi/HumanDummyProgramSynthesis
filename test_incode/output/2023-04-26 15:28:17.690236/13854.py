#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number> [<number> ...]" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        print("Converting %s to %s..." % (number, number + 1))
        
        