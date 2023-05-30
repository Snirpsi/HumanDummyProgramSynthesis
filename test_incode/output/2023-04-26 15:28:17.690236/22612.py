#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split(' ')]
    
    server = HTTPServer(('', 8000), WordsHandler)
    
    print('Serving on port 8000...')
    
    server.serve_forever()

<|/ file filename=word