#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input or adds all ports. """    
    
    ports = input("Enter the ports separated by commas: ")
    ports = ports.split(",")
    
    ports_converted = []
    for port in ports:
        ports_converted.append(int(port))
    
    ports_converted.sort()
    
    print(ports_converted)
    
