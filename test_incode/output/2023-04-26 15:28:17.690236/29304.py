#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or iterates over a port. """    
    port = int(sys.argv[1])
    
    words = []
    
    try:
        server = HTTPServer(('', port), WordsHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    words = [w.strip() for w in server.