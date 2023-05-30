#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = [x.strip() for x in sys.argv[1].split(',')]
    
    server = HTTPServer(('', 8080), WordsServer)
    
    print('Serving on port 8080')
    server.serve_forever()
    
