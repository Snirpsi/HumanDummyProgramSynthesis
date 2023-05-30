#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that adds a port.
    #The port is then listened on.
    server = socketserver.TCPServer(("", port), MyHandler)
    print("Server listening on port {}".format(port))
    server.serve_forever()

