#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    # Open a port on localhost
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()
