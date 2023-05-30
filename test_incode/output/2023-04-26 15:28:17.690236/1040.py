#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    words = ['cat', 'dog', 'mouse']
    
    server = HTTPServer(("", 80), WordsHandler)
    
    server.serve_forever()
    
