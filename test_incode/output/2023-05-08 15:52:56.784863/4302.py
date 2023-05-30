#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that calculates user input.
    #It expects two arguments: port and path.
    #The port number must be accessible from the outside.
    #The path can be any valid file path.
    #The webserver will serve the file from that path.
    import sys
    port = sys.argv[1]
    path = sys.argv[2]
    webserver(port, path)

