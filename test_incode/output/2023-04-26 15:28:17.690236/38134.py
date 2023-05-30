#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and iterates over fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), FruitServer)
    server.serve_forever()
    
