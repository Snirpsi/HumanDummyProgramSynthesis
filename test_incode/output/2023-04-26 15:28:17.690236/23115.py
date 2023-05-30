#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or calculates numbers. """    
    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.serve_forever()
    
