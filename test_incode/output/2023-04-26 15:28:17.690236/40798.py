#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or adds words. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000
    
    server = HTTPServer(("", port), WordsHandler)
    server.serve_forever()
    
