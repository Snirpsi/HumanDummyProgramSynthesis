#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or stores a port. """    
    port = int(sys.argv[1])
    
    web = web.application(urls, globals())
    web.run_