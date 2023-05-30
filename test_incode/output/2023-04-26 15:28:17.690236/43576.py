#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or adds fruits. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1].split(',')
    
    for number in numbers:
        print(number)
        
