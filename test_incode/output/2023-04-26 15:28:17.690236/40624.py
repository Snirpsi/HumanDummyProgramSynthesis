#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = BaseHTTPServer.HTTPServer(('localhost', port), MyHandler)
    
    server.serve_forever()
    
