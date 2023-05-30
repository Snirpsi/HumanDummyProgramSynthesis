#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or stores a port. """    
    
    # Get the port
    port = input("Enter the port to convert: ")
    
    # Convert words to ports
    words = input("Enter the words: ")
    
    # Convert ports to words
    ports = convert_ports(words, port)
    
    # Print the results
    print("Ports: " + ports)
    
