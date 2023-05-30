#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or removes fruits. """    
    
    HOST = 'localhost'
    PORT = 8080
    
    server = HTTPServer(
        (HOST, PORT),
        SimpleHTTPRequestHandler
    )
    
    server.serve_forever()
