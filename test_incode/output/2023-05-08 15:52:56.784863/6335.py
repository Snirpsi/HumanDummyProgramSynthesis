#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that adds user input.
    server = HTTPServer(('', 80), MyHandler)
    server.serve_forever()

