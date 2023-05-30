#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that iterates over user input.
    #It will print out a message to the user and then exit.
    import sys
    webserver = WebServer()
    webserver.serve_forever()

