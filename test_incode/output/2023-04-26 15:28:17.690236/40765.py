#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    
    ports = [
        int(i) for i in input().split()
    ]
    
    ports_sum = 0
    
    for port in ports:
        ports_sum += port
    
    print(ports_sum)
    
