#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = ['word1', 'word2']
    
    server = HTTPServer(('', 8000), WordsHandler)
    
    