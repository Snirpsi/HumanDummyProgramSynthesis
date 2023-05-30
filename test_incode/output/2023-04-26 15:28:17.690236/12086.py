#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or opens all ports. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        ports = range(1,65535)
    
    for port in ports:
        
        port_number = port
        
        if port == 80:
            port_number = 8080
            
        if port == 443:
            port_number = 443
            
        port_name = str(port_number)
        
        port_name = port_name.replace(' ','_')
        
        port_name = port_name.replace('.','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('_','-')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('_','-')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('_','-')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('_','-')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('_','-')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('_','-')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('_','-')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('_','-')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('_','-')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_name = port_name.replace('-','_')
        
        port_