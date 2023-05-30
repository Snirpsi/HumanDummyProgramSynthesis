#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or prints numbers. """    
    ports = range(65535)
    for port in ports:
        print(port)
