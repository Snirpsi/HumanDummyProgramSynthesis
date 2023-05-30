#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or removes all ports. """    
    while True:
        try:
            ports = input("Enter a port number: ")
            ports = [int(i) for i in ports.split()]
            ports = ports[:]
            ports.remove(0)
            ports.sort()
            ports = list(map(str, ports))
            ports = " ".join(ports)
            print(ports)
            
        except EOFError:
            break
        
