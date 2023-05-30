#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    # Start the server
    httpd = HTTPServer(('', 80), RequestHandler)
    
    # Run the server
    httpd.serve_forever()
    
