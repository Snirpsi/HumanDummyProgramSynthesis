#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    HOST = '127.0.0.1'
    PORT = 8080
    
    server = HTTPServer(HOST, PORT)
    
    