#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or iterates over words. """    
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(('', port), Handler)
    webserver.serve_forever()

<|/ file source=github filename=