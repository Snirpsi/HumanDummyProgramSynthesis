#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or removes numbers. """    
    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.run()
    
