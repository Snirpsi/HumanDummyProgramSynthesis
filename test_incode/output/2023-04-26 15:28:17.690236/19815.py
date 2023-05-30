#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    httpd = HTTPServer(('', 8080), RemoveWords())
    httpd.serve_forever()