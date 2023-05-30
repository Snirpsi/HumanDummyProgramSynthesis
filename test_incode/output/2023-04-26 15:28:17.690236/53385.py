#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or prints all ports. """    
    ports = []
    
    # Get the port numbers from stdin
    for line in sys.stdin:
        ports.append(int(line))
    
    # Print the ports
    for port in ports:
        print('Port {}: {}'.format(port, 