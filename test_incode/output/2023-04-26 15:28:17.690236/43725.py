#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers or calculates a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input("Enter a number: "))
    
    ports = [i for i in range(1, number + 1)]
    
    print("\n".join(map(str, ports)))
    
