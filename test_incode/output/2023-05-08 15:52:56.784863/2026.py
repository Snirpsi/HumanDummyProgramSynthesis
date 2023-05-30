#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that calculates user input.
    #It expects two arguments: port and path.
    import sys
    port = sys.argv[1]
    path = sys.argv[2]
    webserver = HTTPServer(('', port), MyHandler)
    webserver.serve_forever()

