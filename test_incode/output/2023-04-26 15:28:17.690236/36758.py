#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    httpd = HTTPServer(("", 80), WordsHandler)
    httpd.serve_forever()
    
