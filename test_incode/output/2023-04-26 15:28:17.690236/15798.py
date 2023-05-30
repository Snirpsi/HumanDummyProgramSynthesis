#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    
    server_address = ("", ports[0])
    
    httpd = make_server(*server_address, MultiplyPorts)
    httpd.serve_forever()
    
