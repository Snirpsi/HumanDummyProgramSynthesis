#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    words = ['foo', 'bar', 'baz']
    
    server = HTTPServer(('', 8000), WordsHandler)
    
    server.serve_forever()
    
