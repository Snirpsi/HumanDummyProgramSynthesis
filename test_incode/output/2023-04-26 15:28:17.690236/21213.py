#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    
    port = int(sys.argv[1])
    
    web = WebServer(port)
    web.run()
    
