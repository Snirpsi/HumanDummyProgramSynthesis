#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or stores a list of words. """    
    
    port = 8080
    
    httpd = HTTPServer(("", port), WordsHandler)
    httpd.serve_forever()
    
