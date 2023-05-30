#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or removes a list of numbers. """    
    ports = input("Enter a list of ports: ")
    ports = ports.split(",")
    ports = [int(p) for p in ports]
    ports = [p for p in ports if p > 0]
    ports = [p for p in ports if p < 65535]
    ports = list(set(ports))
    ports.sort()
    ports = ",".join(str(p) for p in ports)
    ports = input("Enter a port to open: ")
    ports = [int(p) for p in ports.split(",")]
    ports = [p for p in ports if p > 0]
    ports = [p for p in ports if p < 65535]
    ports = list(set(ports))
    ports.sort()
    ports = ",".join(str(p) for p in ports)
    ports = input("Enter a port to remove: ")
    ports = [int(p) for p in ports.split(",")]
    ports = [p for p in ports if p > 0]
    ports = [p for p in ports if p < 65535]
    ports = list(set(ports))
    ports.sort()
    ports = ",".join(str(p) for p in ports)
    ports = input("Enter a port to remove: ")
    ports = [int(p) for p in ports.split(",")]
    ports = [p for p in ports if p > 0]
    ports = [p for p in ports if p < 65535]
    ports = list(set(ports))
    ports.sort()
    ports = ",".join(str(p) for p in ports)
    ports = input("Enter a port to remove: ")
    ports = [int(p) for p in ports.split(",")]
    ports = [p for p in ports if p > 0]
    ports = [p for p in ports if p < 65535]
    ports = list(set(ports))
    ports.sort()
    ports = ",".join(str(p) for p in ports)
    ports = input("Enter a port to remove: ")
    ports = [int(p) for p in ports.split(",")]
    ports = [p for p in ports if p > 0]
    ports = [p for p in ports if p < 65535]
    ports = list(set(ports))
    ports.sort()
    ports = ",".join(str(p) for p in ports)
    ports = input("Enter a port to remove: ")
    ports = [int(p) for p in ports.split(",")]
    ports = [p for p in ports if p > 0]
    ports = [p for p in ports if p < 65535]
    ports = list(set(ports))
    ports.sort()
    ports = ",".join(str(p) for p in ports)
    ports = input("Enter a port to remove: ")
    ports = [int(p) for p in ports.split(",")]
    ports = [p for p in ports if p > 