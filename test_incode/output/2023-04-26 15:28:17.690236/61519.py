#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    
    words = ['cat', 'dog', 'mouse', 'elephant', 'bird', 'cat', 'dog', 'mouse', 'elephant', 'bird']
    
    server = HTTPServer(('', 8080), WordsHandler)
    
    