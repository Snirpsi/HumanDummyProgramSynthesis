#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words and stores words. """    
    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    server = HTTPServer(("", 80), WordsHandler)
    
    server.serve_forever()
    
