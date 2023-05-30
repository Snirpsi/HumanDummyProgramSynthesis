#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and iterates over a list of words. """    
    
    words = ['the', 'cat', 'jumps', 'over', 'the', 'dog']
    
    server = HTTPServer(('', 8080), WordsHandler)
    
    print('Serving on port 8080')
    
    server.serve_forever()
    
