#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
