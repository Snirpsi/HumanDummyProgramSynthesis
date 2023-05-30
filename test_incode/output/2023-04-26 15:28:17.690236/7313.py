#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    port = 8080
    httpd = make_server('localhost', port, application)
    httpd.serve_forever()
