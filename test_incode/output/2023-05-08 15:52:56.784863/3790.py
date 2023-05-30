#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

