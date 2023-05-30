#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    words = ['cat', 'dog', 'bird', 'cat', 'dog', 'bird']
    
    server = HTTPServer(("", 80), WordsHandler)
    
    server.serve_forever()
    
