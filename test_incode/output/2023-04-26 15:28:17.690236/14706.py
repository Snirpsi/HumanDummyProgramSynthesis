#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    import sys
    port = int(sys.argv[1])
    web = HTTPServer(('localhost', port), NumbersHandler)
    web.serve_forever()
