#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports or calculates a port. """    
    ports = remove_ports(sys.argv[1])
    ports = calculate_ports(ports)
    
    for port in ports:
        port_name = port['name']
        port_type = port['type']
        port_value = port['value']
        
        print('Port Name: ' + port_name)
        print('Port Type: ' + port_type)
        print('Port Value: ' + port_value)
        
