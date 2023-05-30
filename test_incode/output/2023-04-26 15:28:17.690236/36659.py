#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['word1', 'word2', 'word3']
    
    server = WSGIServer(('', 80), WordsHandler)
    server.serve_forever()

<|/ file filename=