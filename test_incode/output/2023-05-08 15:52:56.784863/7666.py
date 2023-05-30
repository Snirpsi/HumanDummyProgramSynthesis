#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that stores user input.
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

