#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that prints ports.
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    for port in ports:
        server.socket = ssl.wrap_socket(server.socket, certfile='cert.pem', server_side=True)
        server.socket.listen(port)
    print("Listening on port", port)
    server.serve_forever()

