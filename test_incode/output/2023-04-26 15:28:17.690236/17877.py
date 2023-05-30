#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or calculates all ports. """    
    ports = [int(i) for i in raw_input().split()]
    ports.sort()
    
    ports_sum = 0
    for i in ports:
        ports_sum += i
    
    print(ports_sum)
    
