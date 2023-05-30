#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and prints a port. """    
    
    httpd = HTTPServer(("", 80), NumbersHandler)
    httpd.serve_forever()
