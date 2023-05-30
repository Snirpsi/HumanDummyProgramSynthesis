#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    words = ['cat', 'dog', 'mouse', 'rain', 'water', 'tree']
    
    server = HTTPServer(('', 8080), WordsHandler)
    
    print('Starting server...')
    server.serve_forever()
    
