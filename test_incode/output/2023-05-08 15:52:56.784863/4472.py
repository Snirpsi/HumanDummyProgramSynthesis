#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that iterates over ports.
    server = HTTPServer(('', 0), MyHandler)
    server.serve_forever()

