#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and enumerates a list of numbers. """    
    ports = enumerate_ports()
    numbers = enumerate_numbers(ports)
    
    # Print the ports and numbers to stdout
    print("Ports:", ports)
    print("Numbers:", numbers)
    
    # Print the ports and numbers to stderr
    sys.stderr.write("Ports: