#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    port = int(sys.argv[1])
    web = HTTPServer(('', port), Handler)
    web.serve_forever()
