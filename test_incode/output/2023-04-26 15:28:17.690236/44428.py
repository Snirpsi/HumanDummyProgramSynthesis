#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports. """    
    ports = [
        int(port) for port in sys.argv[1:]
    ]
    
    ports_converted = [
        convert_port(port) for port in ports
    ]
    
    ports_converted.sort(key=lambda x: x[1])
    
    for port in ports_converted:
        print(port)
    
