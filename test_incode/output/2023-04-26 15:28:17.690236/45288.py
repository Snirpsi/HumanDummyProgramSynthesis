#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers and removes fruits. """    
    
    port = int(sys.argv[1])
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    server = HTTPServer(('', port), FruitServer)
    
    server.serve_forever()
