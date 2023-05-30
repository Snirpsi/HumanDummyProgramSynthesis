#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    
    # Start a web server
    httpd = HTTPServer(('', 8080), MyHandler)
    
    # Start the server
    httpd.serve_forever()
    
