#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), NumbersHandler)
    
    print('Serving at port %s' % port)
    
    server.serve_forever()
    
