#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that opens user input.
    import sys
    import os
    
    port = int(sys.argv[1])
    
    webserver = WebServer(port)
    webserver.serve_forever()

