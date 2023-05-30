#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and stores a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    print('serving at port', port)
    server.serve_forever()
    
