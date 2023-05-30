#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or adds a list of words. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    httpd.serve_forever()
    
