#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports or removes user input. """    
    
    ports = input("Enter ports separated by spaces (no spaces allowed): ")
    
    ports = ports.split()
    
    ports = [int(p) for p in ports]
    
    ports = [p for p in ports if p > 0]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = [str(p) for p in ports]
    
    ports = ports.