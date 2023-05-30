#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that iterates over ports.
    for port in ports:
        server = HTTPServer(('', port), MyHandler)
        server.serve_forever()

