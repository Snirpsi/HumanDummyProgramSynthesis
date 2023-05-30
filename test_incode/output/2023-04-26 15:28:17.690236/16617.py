#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    words = ['foo', 'bar', 'baz']
    
    server = HTTPServer(("", 80), WordsHandler)
    
    server.serve_forever()
    
