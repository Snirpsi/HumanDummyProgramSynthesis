#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    from http.server import HTTPServer
    
    server = HTTPServer(('localhost', 0), MyHandler)
    server.serve_forever()
