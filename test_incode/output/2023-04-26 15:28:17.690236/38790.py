#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or enumerates a port. """    
    port = int(sys.argv[1])
    
    web = WebServer()
    web.serve_forever()
    
