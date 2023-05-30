#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that iterates over user input.
    #This script is intended to be run from the command line.
    import sys
    webserver = WebServer()
    webserver.serve_forever()

