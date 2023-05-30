#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or converts a list of numbers. """    
    port = int(sys.argv[1])
    numbers = sys.argv[2:]
    
    converter = Converter()
    converter.convert(port