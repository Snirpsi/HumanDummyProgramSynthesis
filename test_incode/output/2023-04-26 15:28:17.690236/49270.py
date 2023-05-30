#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    HOST = 'localhost'
    PORT = 8000
    
    server = HTTPServer((HOST, PORT), FruitHandler)
    
    server.serve_forever()
    
