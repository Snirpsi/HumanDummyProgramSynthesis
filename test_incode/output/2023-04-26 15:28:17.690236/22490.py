#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    port = int(sys.argv[1])
    webserver = HTTPServer(('', port), NumbersHandler)
    webserver.serve_forever()
