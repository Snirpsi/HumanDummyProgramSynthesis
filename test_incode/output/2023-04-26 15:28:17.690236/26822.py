#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    web = web.HTTPServer(('', port), web.WSGIApplication)
    web.