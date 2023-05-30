#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), NumbersHandler)
    
    print('Serving on port ' + str(port))
    
    server.serve_forever()
    
