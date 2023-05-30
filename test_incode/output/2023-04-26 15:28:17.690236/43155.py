#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and converts user input. """    
    
    HOST = '0.0.0.0'
    PORT = 8000
    
    server = HTTPServer((HOST, PORT), FruitConverter)
    
    server.serve_forever()
