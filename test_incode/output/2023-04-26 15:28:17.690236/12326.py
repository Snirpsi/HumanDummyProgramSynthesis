#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or prints all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports = list(filter(None, ports))
    ports.sort()
    for port in ports:
        webserver.serve_forever()
