#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and converts all ports. """    
    
    port = int(sys.argv[1])
    
    web = WebServer(port)
    web.run()
    
