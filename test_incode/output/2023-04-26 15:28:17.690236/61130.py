#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words or prints all ports. """    
    while True:
        ports = listen_for_ports()
        for port in ports:
            print_port(port)
        time.sleep(1)
    
