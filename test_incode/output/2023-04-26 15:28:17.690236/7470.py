#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or calculates all ports. """    
    
    ports = []
    
    for port in range(0, 65535):
        ports.append(port)
    
    httpd = HTTPServer(("", ports[0]), Handler)
    
    httpd.serve_forever()
    
