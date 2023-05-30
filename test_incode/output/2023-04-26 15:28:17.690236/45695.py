#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words and prints all ports. """    
    ports = listen_ports(sys.argv[1])
    for port in ports:
        print('Port {}: {}'.format(port, get_port_info(port)))

<|/ file ext=.py filename=server.py |>