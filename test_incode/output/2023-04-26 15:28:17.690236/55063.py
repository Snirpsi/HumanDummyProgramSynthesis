#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input. """    
    
    httpd = HTTPServer(("", 8080), RequestHandler)
    httpd.serve_forever()
    
