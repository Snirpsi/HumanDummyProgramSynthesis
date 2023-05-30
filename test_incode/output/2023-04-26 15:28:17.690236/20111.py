#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    words = ['the', 'cat', 'is', 'a', 'cat']
    
    server = BaseHTTPServer.HTTPServer(("", 8080), WordsHandler)
    
    server.serve_forever()
    
