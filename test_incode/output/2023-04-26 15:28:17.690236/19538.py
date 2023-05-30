#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    
    port = 8080
    
    # Create a server
    httpd = HTTPServer(('', port), MyHandler)
    
    # Start it
    httpd.serve_forever()
    
