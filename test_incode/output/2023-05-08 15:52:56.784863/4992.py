#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    import sys
    import os
    webserver = WSGIServer(('', 8000), app)
    webserver.serve_forever()

