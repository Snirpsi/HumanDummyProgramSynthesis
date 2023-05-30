#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and prints all ports. """    
    ports = []
    
    # Iterate over all words and print their ports
    for word in words:
        ports.append(get_port(word))
    
    # Print the ports
    print(ports)
    
    # Close the ports
    for port in ports:
        port.close()
    
    # Close the webserver
    webserver.