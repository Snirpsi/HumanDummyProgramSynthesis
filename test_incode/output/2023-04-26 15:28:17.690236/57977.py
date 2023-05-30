#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    words = ['word1', 'word2', 'word3', 'word4']
    
    port = 5000
    
    server = HTTPServer(('', port), WordsHandler)
    
    server.serve_forever()
    
