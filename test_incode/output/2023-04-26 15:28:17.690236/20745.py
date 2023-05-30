#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words or enumerates all ports. """    
    
    ports = []
    
    # Parse command line arguments
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    
    # Start server
    
    httpd = make_server('', 8000, make_handler_for_ports(ports))
    httpd.serve_forever()
    
