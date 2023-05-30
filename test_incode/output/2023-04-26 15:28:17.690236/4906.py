#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = range(8080, 8100)
    
    httpd = HTTPServer(('localhost', ports[0]), Handler)
    httpd.serve_forever()
