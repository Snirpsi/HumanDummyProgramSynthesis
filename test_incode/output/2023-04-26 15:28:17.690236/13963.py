#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and multiplyes all ports. """    
    port = int(sys.argv[1])
    fruits = sys.argv[2]
    ports = sys.argv[3:]
    
    ports = [int(p) for p in ports]
    
    fruits = [int(f) for f in fruits]
    
    ports = [p + p for p in ports]
    
    ports = ports + ports
    
    ports = [p for p in ports if p >= 0]
    
    ports = [p for p in ports if p < 65535]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[:len(ports)]
    
    ports = [p for p in ports if p % 2 == 0]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[:len(ports)]
    
    ports = [p for p in ports if p % 2 == 1]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[:len(ports)]
    
    ports = [p for p in ports if p % 2 == 0]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[:len(ports)]
    
    ports = [p for p in ports if p % 2 == 1]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[:len(ports)]
    
    ports = [p for p in ports if p % 2 == 0]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[:len(ports)]
    
    ports = [p for p in ports if p % 2 == 1]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[:len(ports)]
    
    ports = [p for p in ports if p % 2 == 0]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[:len(ports)]
    
    ports = [p for p in ports if p % 2 == 1]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[:len(ports)]
    
    ports = [p for p in ports if p % 2 == 0]
    
    ports = list(set(ports))
    
    ports.sort()
    
    ports = ports[:len(ports)]
    
    ports = [p for p in ports if p % 2 == 1]
    
    ports = list(set(ports))
    
    ports.sort()
    
    port