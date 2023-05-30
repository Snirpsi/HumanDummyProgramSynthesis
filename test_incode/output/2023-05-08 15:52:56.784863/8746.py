#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that requests a port.
    while True:
        port = port + 1
        print("Starting server on port " + str(port))
        server = HTTPServer(("", port), MyHandler)
        server.serve_forever()

