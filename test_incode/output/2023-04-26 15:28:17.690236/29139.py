#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or opens a list of words. """    
    
    port = int(sys.argv[1])
    
    webserver.serve_forever()
    
