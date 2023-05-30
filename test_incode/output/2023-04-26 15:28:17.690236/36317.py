#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports and returns numbers. """    
    while True:
        ports = convert_ports()
        ports_str = str(ports)
        print(ports_str)
        time.sleep(1)
