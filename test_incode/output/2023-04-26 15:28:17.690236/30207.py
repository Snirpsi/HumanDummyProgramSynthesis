#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports. """    
    ports = find_ports()
    
    for port in ports:
        
        port_name = port[0]
        
        port_data = get_port_data(port_name)
        
        if port_data is not None:
            
            port_data['port'] = port[1]
            
            port_data['port_name'] = port_name
            
            port_data['port_type'] = port_data['port_type'].lower()
            
            port_data['port_type'] = port_data['port_type'].upper()
            
            port_data['port_type'] = port_data['port_type'].replace(' ', '_')
            
            port_data['port_type'] = port_data['port_type'].replace('-', '_')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['port_type'] = port_data['port_type'].replace('_', '-')
            
            port_data['