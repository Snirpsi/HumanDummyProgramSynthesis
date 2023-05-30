#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    
    import sys
    
    port = sys.argv[1]
    
    server = HTTPServer(("", port), WordsHandler)
    
    print("Serving on port {}".format(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print("