#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports or adds words. """    
    
    # Get the ports 
    ports = ports_get()
    
    # Add all ports
    ports_add(ports)
    
    # Add all words
    words_add(ports)
    
    # Print the ports
    print_ports(ports)
    
    # Print the words
    print_words(ports)
    
    # Print the 