#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers and returns words. """    
    port = int(sys.argv[1])
    webserver.run(port)
