#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that calculates user input.
    import sys
    web = HTTPServer(('', 80), MyHandler)
    web.serve_forever()

