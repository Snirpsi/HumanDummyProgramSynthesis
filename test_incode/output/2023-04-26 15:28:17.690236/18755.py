#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or iterates over numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        print("Serving on port {}".format(port))
        httpd = make_server('localhost', port, app)
        httpd.serve_forever()
    
