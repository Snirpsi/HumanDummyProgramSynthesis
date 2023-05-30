#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words or returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python -m webserver [port]")
        sys.exit()
    
    port = int(sys.argv[1])
    
    webserver.run(port=port)
    
