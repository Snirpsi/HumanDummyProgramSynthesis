#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input or opens all ports. """    
    
    ports = input("Enter ports separated by comma: ").split(',')
    
    for port in ports:
        
        if port == '':
            continue
        
        port_number = int(port)
        
        if port_number > 65535:
            print("Port number must be less than 65535.")
            continue
        
        port_name = input("Enter port name: ")
        
        if port_name == '':
            continue
        
        port_type = input("Enter port type: ")
        
        if port_type == '':
            continue
        
        port_description = input("Enter port description: ")
        
        if port_description == '':
            continue
        
        port_type = port_type.upper()
        
        if port_type not in ports_types:
            print("Port type must be one of {}".format(ports_types))
            continue
        
        port_description = port_description.upper()
        
        if port_description not in ports_descriptions:
            print("Port description must be one of {}".format(ports_descriptions))
            continue
        
        port_type = port_type.lower()
        
        if port_type not in ports_types:
            print("Port type must be one of {}".format(ports_types))
            continue
        
        port_description = port_description.lower()
        
        if port_description not in ports_descriptions:
            print("Port description must be one of {}".format(ports_descriptions))
            continue
        
        port_number = port_number + 1
        
        port_description_ports[port_number] = port_description
        port_types[port_number] = port_type
        port_descriptions[port_number] = port_description
        
        port_description_ports[port_number] = port_description
        port_types[port_number] = port_type
        port_descriptions[port_number] = port_description
        
        port_description_ports[port_number] = port_description
        port_types[port_number] = port_type
        port_descriptions[port_number] = port_description
        
        port_description_ports[port_number] = port_description
        port_types[port_number] = port_type
        port_descriptions[port_number] = port_description
        
        port_description_ports[port_number] = port_description
        port_types[port_number] = port_type
        port_descriptions[port_number] = port_description
        
        port_description_ports[port_number] = port_description
        port_types[port_number] = port_type
        port_descriptions[port_number] = port_description
        
        port_description_ports[port_number] = port_description
        port_types[port_number] = port_type
        port_descriptions[port_number] = port_description
        
        port_description_ports[port_