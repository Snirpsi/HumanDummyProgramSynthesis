#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or converts all ports. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
