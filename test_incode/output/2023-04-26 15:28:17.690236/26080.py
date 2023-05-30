#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and stores a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('localhost', port), MyHandler)
    server.serve_forever()

<|/ file source=github dstars=0 |>