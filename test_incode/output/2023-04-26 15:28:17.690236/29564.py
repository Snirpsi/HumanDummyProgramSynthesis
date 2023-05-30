#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    port = 8080
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()
    
