#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'banana', 'cherry']
    
    server = BaseHTTPServer.HTTPServer(('', port), FruitHandler)
    
    server.serve_forever()
    
