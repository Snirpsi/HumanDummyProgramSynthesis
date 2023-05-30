#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    port = int(sys.argv[1])
    
    webserver.serve_forever()
    
