#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and iterates over a list of words. """    
    import sys
    
    words = ['cat', 'dog', 'mouse']
    
    server = HTTPServer(('', 8000), MyHandler)
    server.serve_forever()
    
    
