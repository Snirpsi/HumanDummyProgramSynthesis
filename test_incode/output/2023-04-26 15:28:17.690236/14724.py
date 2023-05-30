#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    words = ['foo', 'bar', 'baz', 'qux', 'quux', 'quuux']
    
    server = HTTPServer(('', 8000), WordsHandler)
    
    server.serve_forever()
    
