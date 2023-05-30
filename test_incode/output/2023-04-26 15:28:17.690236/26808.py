#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    words = ['word1', 'word2']
    
    # Create a server
    server = HTTPServer(("", 80), WordsHandler)
    
    # Start it
    server.serve_forever()
    
