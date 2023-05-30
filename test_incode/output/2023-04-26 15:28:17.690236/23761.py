#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    port = 8000
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
