#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port and converts all ports. """    
    ports = sys.argv[1:]
    ports = [int(p) for p in ports]
    
    ports_converted = []
    for port in ports:
        ports_converted.append(convert_port(port))
    
    print('\n'.join(ports_converted))

<|/ file ext=.py source=github filename=port