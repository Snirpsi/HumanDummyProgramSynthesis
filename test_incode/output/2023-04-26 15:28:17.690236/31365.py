#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or enumerates a list of numbers. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()
