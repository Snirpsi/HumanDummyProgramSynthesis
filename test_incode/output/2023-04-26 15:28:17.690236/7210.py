#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers or returns a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    web = WebServer(port)
    web.run()
    
