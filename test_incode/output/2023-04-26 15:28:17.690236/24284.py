#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports or removes a list of numbers. """    
    ports = []
    ports_remove = []
    
    ports_remove = input("Enter a list of numbers to remove: ")
    
    ports = input("Enter a list of numbers to add: ")
    
    ports_remove = ports_remove.split(",")
    
    ports_remove = map(int, ports_remove)
    
    ports_remove = list(set(ports_remove))
    
    ports_remove.sort()
    
    ports_remove = map(str, ports_remove)
    
    ports_remove = ",".join(ports_remove)
    
    ports_remove = input("Enter the ports to remove: ")
    
    ports_remove = ports_remove.split(",")
    
    ports_remove = map(int, ports_remove)
    
    ports_remove = list(set(ports_remove))
    
    ports_remove.sort()
    
    ports_remove = map(str, ports_remove)
    
    ports_remove = input("Enter the ports to add: ")
    
    ports_remove = ports_remove.split(",")
    
    ports_remove = map(int, ports_remove)
    
    ports_remove = list(set(ports_remove))
    
    ports_remove.sort()
    
    ports_remove = map(str, ports_remove)
    
    ports_remove = input("Enter the ports to add: ")
    
    ports_remove = ports_remove.split(",")
    
    ports_remove = map(int, ports_remove)
    
    ports_remove = list(set(ports_remove))
    
    ports_remove.sort()
    
    ports_remove = map(str, ports_remove)
    
    ports_remove = input("Enter the ports to add: ")
    
    ports_remove = ports_remove.split(",")
    
    ports_remove = map(int, ports_remove)
    
    ports_remove = list(set(ports_remove))
    
    ports_remove.sort()
    
    ports_remove = map(str, ports_remove)
    
    ports_remove = input("Enter the ports to add: ")
    
    ports_remove = ports_remove.split(",")
    
    ports_remove = map(int, ports_remove)
    
    ports_remove = list(set(ports_remove))
    
    ports_remove.sort()
    
    ports_remove = map(str, ports_remove)
    
    ports_remove