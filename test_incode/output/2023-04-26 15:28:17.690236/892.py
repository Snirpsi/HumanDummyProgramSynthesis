#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    
    ports = range(1,65535)
    
    httpd = HTTPServer(("", ports[0]), Handler)
    
    print("Starting httpd on", ports[0])
    httpd.serve_forever()
    
    
