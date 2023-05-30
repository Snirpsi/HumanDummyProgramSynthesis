#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = range(1,65535)
    
    httpd = HTTPServer(('localhost', ports[0]), Handler)
    httpd.serve_forever()
    
