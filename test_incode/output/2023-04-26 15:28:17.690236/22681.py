#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers or stores a list of words. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    