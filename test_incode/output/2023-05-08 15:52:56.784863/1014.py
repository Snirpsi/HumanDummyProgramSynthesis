#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    import sys
    webserver = HTTPServer(('', 80), RequestHandler)
    webserver.serve_forever()

