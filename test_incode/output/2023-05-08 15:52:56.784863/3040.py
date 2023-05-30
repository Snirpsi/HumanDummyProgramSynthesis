#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that removes user input.
    import sys
    import os
    webserver = WSGIServer(('', 8080), app)
    webserver.serve_forever()

