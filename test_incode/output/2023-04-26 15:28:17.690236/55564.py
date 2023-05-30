#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    # Create a server to receive HTTP requests
    httpd = HTTPServer(("", 80), RequestHandler)
    
    # Start a thread to handle each request
    httpd.serve_forever()
    
