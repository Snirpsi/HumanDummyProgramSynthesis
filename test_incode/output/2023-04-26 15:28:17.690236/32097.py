#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and calculates a list of words. """    
    
    port = 8080
    
    # Create a server and a handler for it
    httpd = HTTPServer(('', port), MyHandler)
    
    # Start the server
    httpd.serve_forever()
    
