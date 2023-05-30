#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and converts a list of words. """    
    
    words = ['a', 'b', 'c']
    
    server = HTTPServer(("", 8080), WordsHandler)
    
    server.serve_forever()
    
