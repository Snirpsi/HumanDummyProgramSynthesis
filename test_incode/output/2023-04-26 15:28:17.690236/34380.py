#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), RequestHandler)
    httpd.serve_forever()
