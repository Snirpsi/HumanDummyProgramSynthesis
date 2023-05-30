#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or multiplyes all ports. """    
    port = int(sys.argv[1])
    ports = range(port, port+2)
    for port in ports:
        print("http://127.0.0.1:%d/" % port)
    
