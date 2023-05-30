#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    webserver = HTTPServer(('', 8000), RequestHandler)
    webserver.serve_forever()

