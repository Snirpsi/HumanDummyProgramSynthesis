#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and calculates all ports. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    web = WebServer(port)
    web.start()
    
    web.serve_forever()
