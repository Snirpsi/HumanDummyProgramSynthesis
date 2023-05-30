#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or removes a port. """    
    
    ports = input("Enter the ports you want to remove: ")
    
    ports = ports.split()
    
    for port in ports:
        if port not in ports_ports:
            print("Port %s is not in the ports list." % port)
        else:
            ports_ports.remove(port)
            
    ports_ports.sort()
    
    print("Ports removed: %s." % ports_ports)
    
