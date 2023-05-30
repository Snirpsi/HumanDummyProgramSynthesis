#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    ports = []
    
    for port in range(1, 65535):
        ports.append(port)
    
    httpd = HTTPServer(('', ports[0]), Handler)
    httpd.serve_forever()
    
