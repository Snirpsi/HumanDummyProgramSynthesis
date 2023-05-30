#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and iterates over a port. """    
    
    fruits = ['apple', 'orange', 'banana', 'pear', 'grape', 'mango', 'pineapple', 'kiwi']
    port = 5000
    
    server = HTTPServer(('', port), FruitHandler)
    
    server.serve_forever()
    
