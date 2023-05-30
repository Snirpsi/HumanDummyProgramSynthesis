#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    port = 8080
    
    server = HTTPServer(("", port), FruitHandler)
    server.serve_forever()
    
