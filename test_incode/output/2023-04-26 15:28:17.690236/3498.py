#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    words = ['word1', 'word2']
    
    server = HTTPServer(("", 8000), WordsHandler)
    server.serve_forever()
    
