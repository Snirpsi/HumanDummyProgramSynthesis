#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits or returns a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), FruitServer)
    
    server.serve_forever()
    
