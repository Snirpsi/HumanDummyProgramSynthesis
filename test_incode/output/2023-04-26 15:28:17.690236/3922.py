#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and opens user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), FruitHandler)
    
    server.serve_forever()
    
