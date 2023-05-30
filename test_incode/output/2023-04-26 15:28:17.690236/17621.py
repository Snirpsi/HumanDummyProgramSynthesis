#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input and adds all ports. """    
    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    ports_sum = 0
    
    for port in ports:
        ports_sum += int(port)
    
    print(ports_sum)
    
