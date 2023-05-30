#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and opens all ports. """    
    port = int(sys.argv[1])
    
    # Create a server
    server = HTTPServer(('', port), FruitHandler)
    
    # Start it
    server.serve_forever()
