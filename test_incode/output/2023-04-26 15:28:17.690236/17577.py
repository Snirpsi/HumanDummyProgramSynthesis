#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and converts a port. """    
    port = int(sys.argv[1])
    
    converter = Converter()
    
    converter.convert(port)
    
