#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that converts user input.
    import sys
    import os
    web = WebServer()
    web.serve_forever()

