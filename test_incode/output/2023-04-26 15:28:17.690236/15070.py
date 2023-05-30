#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    words = ['foo', 'bar', 'baz']
    
    port = 5000
    
    server = HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
    
