#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or enumerates all ports. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()
    
