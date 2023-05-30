#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    
    ports = []
    
    # Enumerate all ports
    for port in os.listdir('/sys/class/net/'):
        
        # Ignore non-ports
        if port.isdigit():
            
            # Get port number
            port_number = int(port)
            
            # Add port to list
            ports.append(port_number)
            
    # Print list
    print(ports)
    
    # Call function with ports list
    enumerate_ports(ports)
    
    # Call function with ports list as argument
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit and exit and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit and exit and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as argument and print result and exit and exit and exit and exit and exit and exit
    enumerate_ports(ports)
    
    # Call function with ports list as 