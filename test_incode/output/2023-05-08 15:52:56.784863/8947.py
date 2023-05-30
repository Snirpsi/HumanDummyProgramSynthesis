#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    import sys
    web = HTTPServer(('', 8080), RequestHandler)
    web.serve_forever()

