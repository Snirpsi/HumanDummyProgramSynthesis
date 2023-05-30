#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or calculates words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), WordsHandler)
    
    print('Starting server on port %d' % port)
    
    server.serve_forever()
    
