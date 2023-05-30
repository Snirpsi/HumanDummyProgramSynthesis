#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port or iterates over user input. """    
    port = int(input("Enter a port number: "))
    
    if port > 0:
        ports = [port]
    else:
        ports = range(port)
    
    for port in ports:
        print("The port number {} is {}.".format(port, ports[port]))
        
