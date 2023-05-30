#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports. """    
    
    # Define the port list
    ports = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2', '/dev/ttyACM3', '/dev/ttyACM4']
    
    # Iterate over all ports
    for port in ports:
        
        # Open the port and read its contents
        file = open(port, 'r')
        
        # Print the contents of the port
        print(file.read())
        
        # Close the port
        file.close()
        
    # Close the port list
    file.close()
    
