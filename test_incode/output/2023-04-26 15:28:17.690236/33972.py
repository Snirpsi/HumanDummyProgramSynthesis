#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or opens numbers. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), FruitHandler)
    server.serve_forever()
    
