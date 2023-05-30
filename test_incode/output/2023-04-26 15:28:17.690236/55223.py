#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or converts a port. """    
    
    ports_to_convert = []
    
    while True:
        ports_to_convert.append(input("Enter a port to convert: "))
        
        if ports_to_convert[-1] == "":
            break
    
    ports_to_convert = ports_to_convert[:-1]
    
    for port in ports_to_convert:
        
        try:
            
            port_number = int(port)
            
            if port_number < 0 or port_number > 65535:
                print("Invalid port number")
                continue
            
            port_to_convert = port_number
            
        except ValueError:
            print("Invalid port number")
            continue
        
        
        if port_to_convert not in ports_to_convert:
            print("Port number " + str(port_to_convert) + " is not in ports_to_convert")
            continue
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        