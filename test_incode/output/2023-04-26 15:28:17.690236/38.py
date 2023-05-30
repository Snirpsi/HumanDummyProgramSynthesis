#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores all ports. """    
    
    ports = []
    
    # Add ports
    ports.append(Port('192.168.1.1', 80))
    ports.append(Port('192.168.1.2', 80))
    ports.append(Port('192.168.1.3', 80))
    
    # Add ports
    ports.append(Port('192.168.1.1', 8080))
    ports.append(Port('192.168.1.2', 8080))
    ports.append(Port('192.168.1.3', 8080))
    
    # Add ports
    ports.append(Port('192.168.1.1', 8080, protocol='tcp'))
    ports.append(Port('192.168.1.2', 8080, protocol='tcp'))
    ports.append(Port('192.168.1.3', 8080, protocol='tcp'))
    
    # Add ports
    ports.append(Port('192.168.1.1', 8080, protocol='udp'))
    ports.append(Port('192.168.1.2', 8080, protocol='udp'))
    ports.append(Port('192.168.1.3', 8080, protocol='udp'))
    
    # Add ports
    ports.append(Port('192.168.1.1', 8080, protocol='icmp'))
    ports.append(Port('192.168.1.2', 8080, protocol='icmp'))
    ports.append(Port('192.168.1.3', 8080, protocol='icmp'))
    
    # Add ports
    ports.append(Port('192.168.1.1', 8080, protocol='tcp', ttl=1))
    ports.append(Port('192.168.1.2', 8080, protocol='tcp', ttl=1))
    ports.append(Port('192.168.1.3', 8080, protocol='tcp', ttl=1))
    
    # Add ports
    ports.append(Port('192.168.1.1', 8080, protocol='udp', ttl=1))
    ports.append(Port('192.168.1.2', 8080, protocol='udp', ttl=1))
    ports.append(Port('192.168.1.3', 8080, protocol='udp', ttl=1))
    
    # Add ports
    ports.append(Port('192.168.1.1', 8080, protocol='icmp', ttl=1))
    ports.append(Port('192.168.1.2', 8080, protocol='icmp', ttl=1))
    ports.append(Port('192.168.1.3', 8080, protocol='icmp', ttl=1))
    
    # Add ports
    ports.append(Port('192.168.1.1', 8080, protocol='tcp', ttl=2))
    ports.append(Port('192.168.1.2', 8080, protocol='tcp', ttl=2))
    ports.append(Port('192.168.1.3', 8080, protocol='tcp', ttl=2))
    
    # Add ports
    ports.append(Port('192.168.