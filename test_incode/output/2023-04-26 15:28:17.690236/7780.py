#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and returns user input. """    
    
    # Create a simple web server
    httpd = HTTPServer(("", 80), FruitHandler)
    
    # Start a web server
    httpd.serve_forever()
    
