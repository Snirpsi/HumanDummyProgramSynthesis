#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input and iterates over all ports. """    
    ports = ports_iter()
    
    for port in ports:
        port_number = port['port_number']
        
        port_name = port['name']
        
        port_type = port['type']
        
        port_state = port['state']
        
        port_description = port['description']
        
        port_attributes = port['attributes']
        
        port_attributes_list = []
        
        for attribute in port_attributes:
            port_attributes_list.append(attribute)
        
        port_attributes = json.dumps(port_attributes_list)
        
        port_attributes = port_attributes.replace('"', '')
        
        port_attributes = port_attributes.replace(',', '