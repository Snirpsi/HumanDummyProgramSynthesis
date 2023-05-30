#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    ports_sum = 0
    for port in ports:
        ports_sum += port
    
    print("The sum of all ports is: " + str(ports_sum))
