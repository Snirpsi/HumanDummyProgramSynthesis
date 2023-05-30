#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and converts a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    numbers = [int(number) for number in sys.argv[2:]]
    
    ports_converted = [convert_port(port, numbers) for port in ports]
    
    print('\n'.join(ports_converted))
    
