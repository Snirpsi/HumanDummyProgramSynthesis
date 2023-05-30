#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, NumbersHandler)
    httpd.serve_forever()
