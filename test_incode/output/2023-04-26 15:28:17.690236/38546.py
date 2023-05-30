#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    port = 8080
    
    httpd = HTTPServer(('', port), Number