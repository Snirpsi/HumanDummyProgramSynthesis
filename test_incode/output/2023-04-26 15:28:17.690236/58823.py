#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    words = ['cat', 'dog', 'mouse', 'horse']
    
    server = HTTPServer(('', 8080), WordsHandler)
    
    