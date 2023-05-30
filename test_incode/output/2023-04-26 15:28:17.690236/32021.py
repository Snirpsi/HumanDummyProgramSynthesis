#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print("Starting port {} on {}".format(port, HOST))
        
        httpd = make_server(port, HOST, app)
        httpd.serve_forever()
        
