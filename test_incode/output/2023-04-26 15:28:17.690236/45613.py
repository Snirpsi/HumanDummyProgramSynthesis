#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and returns a port. """    
    
    words = ['cat', 'dog', 'mouse', 'elephant']
    
    port = 5000
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
