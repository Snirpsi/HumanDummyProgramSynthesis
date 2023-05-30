#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    import os
    
    ports = [int(p) for p in os.environ['PORTS'].split(',')]
    
    server_address = ("", ports[0])
    
    httpd = HTTPServer(server_address, Handler)
    
    httpd.serve_forever()
    
