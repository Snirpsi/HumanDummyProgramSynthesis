#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words or removes all ports. """    
    
    ports = input("Enter ports separated by comma: ")
    ports = ports.split(",")
    
    for port in ports:
        
        port = int(port)
        
        if port > 0 and port <= 65535:
            
            port_string = str(port)
            
            port_string = port_string.replace(",", "")
            
            port_string = port_string.replace("-", "")
            
            port_string = port_string.replace(":", "")
            
            port_string = port_string.replace("(", "")
            
            port_string = port_string.replace(")", "")
            
            port_string = port_string.replace("'", "")
            
            port_string = port_string.replace("[", "")
            
            port_string = port_string.replace("]", "")
            
            port_string = port_string.replace("{", "")
            
            port_string = port_string.replace("}", "")
            
            port_string = port_string.replace(",", "")
            
            port_string = port_string.replace("-", "")
            
            port_string = port_string.replace(":", "")
            
            port_string = port_string.replace("(", "")
            
            port_string = port_string.replace(")", "")
            
            port_string = port_string.replace("'", "")
            
            port_string = port_string.replace("[", "")
            
            port_string = port_string.replace("]", "")
            
            port_string = port_string.replace("{", "")
            
            port_string = port_string.replace("}", "")
            
            port_string = port_string.replace("[", "")
            
            port_string = port_string.replace("]", "")
            
            port_string = port_string.replace("{", "")
            
            port_string = port_string.replace("}", "")
            
            port_string = port_string.replace("[", "")
            
            port_string = port_string.replace("]", "")
            
            port_string = port_string.replace("{", "")
            
            port_string = port_string.replace("}", "")
            
            port_string = port_string.replace("[", "")
            
            port_string = port_string.replace("]", "")
            
            port_string = port_string.replace("{", "")
            
            port_string = port_string.replace("}", "")
            
            port_string = port_string.replace("[", "")
            
            port_string = port_string.replace("]", "")
            
            port_string = port_string.replace("{", "")
            
            port_string = port_string.replace("}", "")
            
            port_string = port_string.replace("[", "")
            
            port_string = port_string.replace("]", "")
            
            port_string = port_string.replace("{", "")
            
            port_string = port_string.replace("}", "")
            
            port_string = port_string.replace("[", "")
            
