#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or iterates over a list of words. """    
    
    # Create a simple web server
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8000), RequestHandler)
    
    # Start web server
    httpd.serve_forever()

<|/ file filename=server.py source=github |>