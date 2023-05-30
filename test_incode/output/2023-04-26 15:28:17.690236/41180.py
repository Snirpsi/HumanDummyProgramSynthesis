#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or adds fruits. """    
    
    words = ['apple', 'banana', 'cherry']
    
    server = HTTPServer(('', 8000), WordsHandler)
    server.serve_forever()
