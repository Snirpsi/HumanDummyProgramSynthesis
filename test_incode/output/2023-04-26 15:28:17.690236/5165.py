#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or calculates a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python -m SimpleWebServer <port>")
        sys.exit()
    
    port = int(sys.argv[1])
    
    server = SimpleWebServer(port)
    server.serve_forever()
    
