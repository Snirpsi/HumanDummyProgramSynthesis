#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and iterates over fruits. """    
    ports = range(8000, 8100)
    fruits = ['apple', 'orange', 'banana', 'kiwi']
    
    for port in ports:
        server = HTTPServer(('', port), FruitHandler)
        server.serve_forever()
        
