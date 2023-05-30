#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers. """    
    port = int(sys.argv[1])
    
    numbers = []
    
    server = HTTPServer(('', port), NumbersHandler)
    
    print('Serving at port', port)
    
    server.serve_forever()
    
