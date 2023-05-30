#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers or iterates over a port. """    
    import sys
    
    port = int(sys.argv[1])
    
    ports = [int(i) for i in sys.argv[2:]]
    
    ports_sum = 0
    
    for port in ports:
        ports_sum += port
    
    print(ports_sum)
    
