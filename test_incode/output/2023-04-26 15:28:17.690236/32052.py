#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or calculates words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), FruitServer)
    server.serve_forever()
    
