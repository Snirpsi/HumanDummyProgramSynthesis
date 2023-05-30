#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or opens all ports. """    
    
    httpd = HTTPServer(("", 80), MyHandler)
    httpd.serve_forever()
    
