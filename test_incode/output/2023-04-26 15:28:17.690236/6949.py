#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port. """    
    port = 80
    httpd = make_server('', port, app)
    httpd.serve_forever()
