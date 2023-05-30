#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    HOST = 'localhost'
    PORT = 8080
    
    server = HTTPServer(HOST, PORT)
    
    server.serve_forever()

<|/ file source=github filename=