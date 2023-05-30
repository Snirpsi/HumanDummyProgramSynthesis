#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and removes fruits. """    
    
    words = ['apple', 'banana', 'cherry']
    
    server = HTTPServer(('', 8080), WordsHandler)
    
    server.serve_forever()
    
