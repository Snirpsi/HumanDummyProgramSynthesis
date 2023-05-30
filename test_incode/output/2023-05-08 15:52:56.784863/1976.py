#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that adds ports.
    server = HTTPServer(('',8080), SimpleHTTPRequestHandler)
    for port in ports:
        server.socket = ssl.wrap_socket(server.socket, keyfile='./key.pem', certfile='./cert.pem', server_side=True)
        server.socket.listen(port)
        server.handle_request()

