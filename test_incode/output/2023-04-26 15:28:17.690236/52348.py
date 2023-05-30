#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or iterates over a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        httpd = make_server('', port, app)
        httpd.serve_forever()
    
