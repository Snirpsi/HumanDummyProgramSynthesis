#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    HOST = 'localhost'
    PORT = 8080
    
    server = HTTPServer(
        (HOST, PORT),
        SimpleHTTPRequestHandler
    )
    
    server.serve_forever()
    
