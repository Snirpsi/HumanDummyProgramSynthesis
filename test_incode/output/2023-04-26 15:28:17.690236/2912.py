#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words or converts all ports. """    
    port = int(sys.argv[1])
    
    web = web.HTTPServer(('', port), web.app)
    web.serve_forever()
