#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and returns a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()
    
