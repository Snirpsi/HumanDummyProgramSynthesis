#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    web = web.application(urls, globals())
    web.