#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(0)
    
    webserver.serve_forever()
    
