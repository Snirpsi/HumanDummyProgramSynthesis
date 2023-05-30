#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    server = WSGIServer(('', 80), RemoveWordsHandler)
    
    print('Serving on port 80')
    
    server.serve_forever()

<|/ file filename=remove-words.py source=github ext=.py |>