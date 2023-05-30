#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or converts words. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()
