#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers and prints a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    for x in range(port):
        print("%d" % x)
    
    print("End of program")
    
