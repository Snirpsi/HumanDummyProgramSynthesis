#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or stores user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    print('Serving on port {}'.format(port))
    
    server.serve_forever()
    
