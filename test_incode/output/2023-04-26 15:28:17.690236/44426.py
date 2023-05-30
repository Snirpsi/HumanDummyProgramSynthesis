#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports. """    
    ports = [
        port for port in os.listdir('/sys/class/net/') 
        if port.startswith('eth')
    ]
    
    for port in ports:
        port_number = int(port)
        
        port_name = port.split('eth')[1].split(':')[1]
        
        port_number = str(port_number)
        
        port_number = port_number.zfill(2)
        
        port_name = port_name.zfill(2)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.zfill(3)
        
        port_name = port_name.zfill(3)
        
        port_number = port_number.z