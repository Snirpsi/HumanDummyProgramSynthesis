#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port and adds all ports. """    
    
    ports = []
    
    ports.append( {'port': 80, 'name': 'http', 'protocol': 'tcp', 'description': 'HTTP port', 'type': 'http', 'tags': ['http']} )
    ports.append( {'port': 81, 'name': 'https', 'protocol': 'tcp', 'description': 'HTTPS port', 'type': 'https', 'tags': ['https']} )
    ports.append( {'port': 82, 'name': 'ftp', 'protocol': 'tcp', 'description': 'FTP port', 'type': 'ftp', 'tags': ['ftp']} )
    ports.append( {'port': 83, 'name': 'telnet', 'protocol': 'tcp', 'description': 'Telnet port', 'type': 'telnet', 'tags': ['telnet']} )
    
    for port in ports:
        
        port_name = port['name']
        port_type = port['type']
        port_description = port['description']
        
        port_tags = []
        
        for tag in port['tags']:
            
            port_tags.append( {'tag': tag, 'description': tag, 'type': 'tag', 'name': tag} )
        
        port_obj = {
            'name': port_name,
            'type': port_type,
            'description': port_description,
            'tags': port_tags
        }
        
        ports.append( port_obj )
    
    ports_json = json.dumps( ports, indent = 4, sort_keys = True) 
    
    with open('ports.json', 'w') as outfile:
        outfile.write(ports_json)
    
    print('Ports saved.')
    
