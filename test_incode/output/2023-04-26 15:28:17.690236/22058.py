#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words or stores all ports. """    
    ports = ports_open()
    
    # Print the list of ports
    print(ports)
    
    # Print the list of words on the ports
    for port in ports:
        print(port)
        
    # Print the list of words on the ports except the word '