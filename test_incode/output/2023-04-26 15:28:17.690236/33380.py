#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and calculates a port. """    
    
    # Create a server
    httpd = HTTPServer(("", 80), MyHandler)
    
    # Start it
    httpd.serve_forever()
    
