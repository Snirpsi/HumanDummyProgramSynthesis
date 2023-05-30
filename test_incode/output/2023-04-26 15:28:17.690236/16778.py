#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    words = ["word1", "word2", "word3", "word4"]
    
    server = HTTPServer(("", 80), WordsHandler)
    server.serve_forever()
    
