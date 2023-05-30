#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or prints a list of words. """    
    
    port = 8080
    
    # Open the webserver
    httpd = HTTPServer(('', port), FruitHandler)
    
    # Start the webserver
    httpd.serve_forever()
    
