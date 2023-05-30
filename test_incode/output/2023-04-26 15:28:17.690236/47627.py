#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or stores words. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitApp)
    httpd.serve_forever()
    
