#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that converts user input.
    import sys
    webserver = WebServer()
    webserver.serve_forever()

