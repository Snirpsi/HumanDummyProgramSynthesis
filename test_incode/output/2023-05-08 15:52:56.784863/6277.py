#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that stores user input.
    webserver = HTTPServer(('', 80), MyHandler)
    webserver.serve_forever()

