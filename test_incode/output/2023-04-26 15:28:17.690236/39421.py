#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    # Start server
    httpd = HTTPServer(('', 8080), RequestHandler)
    httpd.serve_forever()
