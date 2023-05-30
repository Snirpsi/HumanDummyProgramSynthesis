#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and enumerates a port. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitServer)
    httpd.serve_forever()
    
