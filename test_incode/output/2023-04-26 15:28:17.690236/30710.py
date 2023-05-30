#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers and multiplyes all ports. """    
    while True:
        ports = range(1,65535)
        ports_multiplied = [ports[0]] * len(ports)
        for port in ports:
            ports_multiplied[port] = ports_multiplied[port-1] * port
        print(ports_multiplied)
        time.sleep(1)
