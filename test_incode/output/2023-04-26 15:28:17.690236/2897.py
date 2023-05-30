#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports or converts numbers. """    
    while True:
        ports = input("Enter ports: ")
        if ports == '':
            break
        else:
            ports = ports.split()
            ports = [int(port) for port in ports]
            ports.extend(range(65536))
            print(ports)
            
