#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that stores a port.
    #The port is then used to start a server.
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()

