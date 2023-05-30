#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and calculates numbers. """    
    
    # Start webserver
    httpd = make_server('', 8000, app)
    httpd.serve_forever()
