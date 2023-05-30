#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and removes words. """    
    
    web = web.HTTPServer(('', 8080), web.RequestHandler)
    web.