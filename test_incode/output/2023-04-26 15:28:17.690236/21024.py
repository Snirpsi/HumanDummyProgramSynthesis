#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    # Open the webserver on port 80
    httpd = HTTPServer(('', 80), FruitHandler)
    
    # Start the webserver
    httpd.serve_forever()
    
