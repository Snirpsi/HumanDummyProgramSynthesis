#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports or returns user input. """    
    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    ports_open = []
    for port in ports:
        if port not in ports_open:
            ports_open.append(port)
    
    for port in ports_open:
        
        port_number = int(port)
        
        if port_number < 0 or port_number > 65535:
            print("Port number must be between 0 and 65535")
        else:
            
            port_name = input("Enter port name: ")
            
            port_open = input("Enter port open: ")
            
            port_open = int(port_open)
            
            if port_open < 0 or port_open > 65535:
                print("Port open must be between 0 and 65535")
            else:
                
                port_open = port_open - port_number
                
                if port_open < 0:
                    port_open = 0
                
                if port_open > 65535:
                    port_open = 65535
                
                port_open = port_open + port_number
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_open % 65535
                
                port_open = port_open / 65535
                
                port_open = port_