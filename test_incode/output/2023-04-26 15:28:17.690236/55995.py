#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and iterates over a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()
