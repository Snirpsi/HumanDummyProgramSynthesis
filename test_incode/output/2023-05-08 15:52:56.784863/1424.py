#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that returns a port.
    server = socketserver.TCPServer(("", port), MyHandler)
    print("serving at port", port)
    server.serve_forever()

