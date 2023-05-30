#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and stores user input. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    print('Serving at port {}'.format(port))
    server.serve_forever()
