#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    import os
    
    words = [w.strip() for w in open('words.txt').readlines()]
    
    port = int(os.environ.get('PORT', 8080))
    
    server = HTTPServer(('', port), WordsHandler)
    
    