#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or prints all ports. """    
    
    ports = [int(port) for port in input("Enter ports separated by comma (no spaces):").split(',')]
    
    for port in ports:
        webserver.serve_forever()
    
