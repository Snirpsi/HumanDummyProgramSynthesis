#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input or removes all ports. """    
    ports = input("Enter the ports you want to remove: ")
    ports = ports.split()
    ports = [int(port) for port in ports]
    ports = [port for port in ports if port not in range(0,65535)]
    print(ports)
    
