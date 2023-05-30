#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    words = ["cat", "dog", "mouse", "cat", "dog", "mouse", "cat", "dog", "mouse"]
    
    server = HTTPServer(('', 8080), WordsHandler)
    