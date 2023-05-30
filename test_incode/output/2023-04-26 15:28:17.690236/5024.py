#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or removes all ports. """    
    
    port = int(sys.argv[1])
    
    web = WebServer()
    web.listen(port)
    
    web.