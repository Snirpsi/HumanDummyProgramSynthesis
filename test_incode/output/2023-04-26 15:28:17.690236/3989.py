#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and adds words. """    
    
    # Start server
    httpd = HTTPServer(('localhost', 8080), FruitConverter)
    httpd.serve_forever()
    
    # Run server
    httpd.