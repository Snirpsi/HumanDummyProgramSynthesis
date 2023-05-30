#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or iterates over a list of numbers. """    
    
    # Open ports
    ports = openports()
    
    # Iterate over ports
    for port in ports:
        
        # Open port and read its content
        port_content = openport(port)
        
        # Print the content
        print(port_content)
        
        # Close the port
        closeport(port)
        
        # Wait a second
        time.sleep(1)
        
    # Close ports
    closeports()
    
