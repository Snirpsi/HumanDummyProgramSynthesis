#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    server = HTTPServer(('', 8000), RequestHandler)
    server.serve_forever()

