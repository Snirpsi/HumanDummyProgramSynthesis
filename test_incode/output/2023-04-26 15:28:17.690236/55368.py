#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or prints fruits. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python webserver.py <port>")
        sys.exit()
    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.serve_forever()
    
