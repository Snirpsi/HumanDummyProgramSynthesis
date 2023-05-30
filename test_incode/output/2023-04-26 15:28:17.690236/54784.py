#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or converts fruits. """    
    
    ports = range(8000, 8100)
    fruits = ['apple', 'banana', 'cherry']
    
    for port in ports:
        webserver.serve_forever(port=port)
        
    for fruit in fruits:
        webserver.