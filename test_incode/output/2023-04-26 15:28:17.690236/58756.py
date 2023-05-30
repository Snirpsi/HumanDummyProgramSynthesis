#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports and iterates over a list of numbers. """    
    
    # Get the port list from the command line
    ports = sys.argv[1:]
    
    # Iterate over all ports
    for port in ports:
        
        # Open the port and get its contents
        port = open(port)
        
        # Iterate over all lines
        for line in port:
            
            # Print the line to the screen
            print(line)
            
            # Close the port and quit the program
            port.close()
            
            # Quit this program
            break
            
    # Close the port
    port.close()
    
    # Quit the program
    sys.exit()
    
