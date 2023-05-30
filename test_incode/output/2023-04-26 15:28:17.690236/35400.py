#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and opens words. """    
    
    port = 8080
    
    httpd = HTTPServer(('localhost', port), WordsHandler)
    httpd.serve_forever()
    
