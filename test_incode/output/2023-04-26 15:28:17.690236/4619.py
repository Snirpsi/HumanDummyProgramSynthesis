#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or stores a list of numbers. """    
    
    port = 8080
    
    # Start the server
    httpd = HTTPServer(('', port), FruitServer)
    httpd.serve_forever()
    
