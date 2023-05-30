#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and prints a list of numbers. """    
    
    fruits = ['apple', 'orange', 'pear', 'banana', 'grape', 'pineapple', 'cherry', 'mango']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), FruitHandler)
    
    server.serve_forever()
    
