#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that adds a port.
    server = socketserver.TCPServer(("", port), MyHandler)
    print("Serving on port {}".format(port))
    server.serve_forever()

