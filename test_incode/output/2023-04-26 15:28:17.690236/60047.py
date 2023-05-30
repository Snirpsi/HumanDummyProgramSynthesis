#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = ['cat', 'dog', 'mouse']
    
    port = 5000
    
    httpd = HTTPServer(("", port), WordsHandler)
    httpd.serve_forever()

<|/ file ext=.py filename=server.py |>