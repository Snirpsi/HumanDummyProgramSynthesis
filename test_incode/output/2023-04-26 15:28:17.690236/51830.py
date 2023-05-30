#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and enumerates a port. """    
    ports = enumeratePorts()
    for port in ports:
        print("Port {} has {} words and {} ports.".format(port, port[1], port[2]))
    
