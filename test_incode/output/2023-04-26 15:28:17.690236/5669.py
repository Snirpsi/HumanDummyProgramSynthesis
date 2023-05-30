#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    import sys
    web = HTTPServer(('', 8080), WordsHandler)
    web.