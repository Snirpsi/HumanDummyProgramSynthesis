#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse', 'cat', 'dog', 'bird', 'snake', 'mouse']
    
    server = HTTPServer(("", 8000), WordsHandler)
    server.serve_forever()
    
