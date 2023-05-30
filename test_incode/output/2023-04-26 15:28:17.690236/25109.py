#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and prints a list of words. """    
    
    httpd = HTTPServer(('', 80), RequestHandler)
    httpd.serve_forever()
