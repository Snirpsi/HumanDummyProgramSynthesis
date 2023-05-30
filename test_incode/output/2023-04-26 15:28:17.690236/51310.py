#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    
    server.serve_forever()
    
