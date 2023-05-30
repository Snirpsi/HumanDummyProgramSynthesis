#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or calculates fruits. """    
    
    port = 8080
    
    server = BaseHTTPServer.HTTPServer(('', port), FruitServer)
    
    server.serve_forever()
    
