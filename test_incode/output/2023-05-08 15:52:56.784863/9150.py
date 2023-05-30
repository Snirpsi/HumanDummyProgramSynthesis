#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that removes ports.
    ports = [p for p in ports if p not in ports]
    for port in ports:
        server = HTTPServer(('', port), MyHandler)
        server.serve_forever()

