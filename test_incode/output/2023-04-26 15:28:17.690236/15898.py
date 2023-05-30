#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or returns a port. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        print("Serving on port %d" % port)
        
        httpd = make_server('', port, app)
        httpd.serve_forever()
        
