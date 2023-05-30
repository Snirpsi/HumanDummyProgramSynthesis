#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or iterates over a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    server.serve_forever()
