#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits or opens all ports. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, FruitServer)
    httpd.serve_forever()
    
