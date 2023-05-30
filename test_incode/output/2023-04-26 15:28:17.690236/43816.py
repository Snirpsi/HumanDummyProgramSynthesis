#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and stores fruits. """    
    
    port = 8080
    
    server = HTTPServer(('', port), FruitServer)
    
    server.serve_forever()
    
