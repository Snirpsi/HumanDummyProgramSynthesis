#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that converts user input.
    #It also serves up static files if requested.
    server = HTTPServer(('', 8000), MyHandler)
    server.serve_forever()

