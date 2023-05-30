#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or adds all ports. """    
    port = int(sys.argv[1])
    
    server = WebServer()
    server.serve_forever()
    
    
