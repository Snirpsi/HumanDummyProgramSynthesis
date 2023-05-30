#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    words = ['hello', 'world']
    
    httpd = HTTPServer(("", 80), WordsHandler)
    httpd.serve_forever()
    
