#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    port = sys.argv[1]
    
    httpd = make_server(port, webapp)
    httpd.serve_forever()
    
