#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s number" % sys.argv[0])
        exit(1)
        
    number = sys.argv[1]
    
    numbers = []
    
    for i in range(number):
        numbers.append(i)
    
    print("\n".join(map(str, numbers)))
    
