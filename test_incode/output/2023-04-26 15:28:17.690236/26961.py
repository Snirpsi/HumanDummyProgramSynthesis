#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and returns words. """    
    words = ['word1', 'word2', 'word3']
    
    # Create a server
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start it
    server.serve_forever()
