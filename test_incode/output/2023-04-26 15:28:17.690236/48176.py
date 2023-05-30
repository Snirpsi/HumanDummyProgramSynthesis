#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or iterates over user input. """    
    
    # Create a web server
    httpd = HTTPServer(('localhost', 8080), FruitHandler)
    
    # Start it
    httpd.serve_forever()
