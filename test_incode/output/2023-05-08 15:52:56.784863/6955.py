#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that adds a port.
    #The port is then listened on.
    server_address = ('', port)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()

