#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    HOST = 'localhost'
    PORT = 8080
    
    server = HTTPServer((HOST, PORT), FruitConverter)
    
    server.serve_forever()
    
