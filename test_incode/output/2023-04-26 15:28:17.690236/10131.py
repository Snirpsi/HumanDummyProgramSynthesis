#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or returns a list of words. """    
    import sys
    port = int(sys.argv[1])
    
    server = WebServer(port)
    server.serve_forever()
    
