#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers and adds all ports. """    
    
    # Open a port scanner 
    scanner = PortScanner()
    
    # Iterate over the list of ports 
    for port in scanner.ports:
        print(port)
        
    # Close the scanner 
    scanner.close()
    
