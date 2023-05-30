#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that converts user input.
    #It also serves static files from /static
    webserver = WebServer()
    webserver.serve_forever()

