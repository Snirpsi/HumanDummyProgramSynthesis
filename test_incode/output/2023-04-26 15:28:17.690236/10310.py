#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    ports = range(1,65535)
    ports_sum = 0
    for port in ports:
        ports_sum += port
    ports_sum = str(ports_sum)
    print(ports_sum)
