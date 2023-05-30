#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    port = int(sys.argv[1])
    webserver.serve_forever()
