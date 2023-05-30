#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()

<|/ file filename=wordserver.py ext=.py |>