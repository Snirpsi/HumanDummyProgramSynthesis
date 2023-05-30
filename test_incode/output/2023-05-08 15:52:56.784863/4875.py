#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that stores ports.
    server = HTTPServer(('',8080), SimpleHTTPRequestHandler)
    for port in ports:
        server.socket = ssl.wrap_socket(server.socket, certfile='./cert.pem', server_side=True, ssl_version=ssl.PROTOCOL_TLSv1)
        server.socket.bind(('',port))
        server.socket.listen(5)
        print('Listening on port {}'.format(port))
    while True:
        server.handle_request()

