#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    httpd = HTTPServer(('', 80), RequestHandler)
    httpd.serve_forever()
